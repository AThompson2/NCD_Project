from django.shortcuts import render, HttpResponse, redirect, \
    get_object_or_404, reverse
from django.contrib import messages

from django.conf import settings
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, DetailView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.template.loader import get_template, render_to_string
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

# PayPal stuff
from paypal.standard.forms import PayPalPaymentsForm


# from . import views
from decimal import Decimal


from Products.models import ProductDB
from checkout.models import Order, LineItem, CartItem
from checkout.forms import CartForm, CheckoutFormOne
from checkout import context_processor, cart, hooks


# WeasyPrint items, django-easy-pdf
import weasyprint
from weasyprint import HTML, CSS
from easy_pdf.views import PDFTemplateView, PDFTemplateResponseMixin
from django.utils.safestring import mark_safe






class CheckoutForm(TemplateView):
    template_name = 'checkout/checkout_form.html'

class CheckoutNew(TemplateView):
    template_name = 'checkout/checkout_new.html'

class CheckOutThankyou(TemplateView):
    template_name = 'checkout/checkout_thankyou.html'

class Cart(TemplateView):
    template_name = 'checkout/cart.html'






def users(request):
    form1 = NewUserForm()

    if request.method == "POST":
        form1 = NewUserForm(request.POST)
        if form1.is_valid():
            form1.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')


    return render(request,'checkout/users.html',{'form1':form1})




# Cart, Checkout views

def checkout_index(request):
    all_products = ProductDB.objects.all()
    return render(request, "checkout/checkout_index.html", {
                                    'all_products': all_products,
                                    })



def show_product(request, product_id, product_slug ):
    product = get_object_or_404(ProductDB, id=product_id)
    all_products = ProductDB.objects.all()


    if request.method == 'POST':
        form = CartForm(request, request.POST)
        if form.is_valid():
            request.form_data = form.cleaned_data
            cart.add_items_to_cart(request)
            return redirect('checkout:show_cart')

    form = CartForm(request, initial={'product_id': product.id})
    return render(request, 'checkout/product_detail.html', {
                                            'product': product,
                                            'form': form,
                                            'all_products': all_products,
                                            })




def show_cart(request):
    all_products = ProductDB.objects.all()

    if request.method == 'POST':
        if request.POST.get('submit') == 'Update':
            cart.update_item(request)
        if request.POST.get('submit') == 'Remove':
            cart.remove_item(request)

    cart_items = cart.get_all_cart_items(request)
    cart_subtotal = cart.subtotal(request)
    return render(request, 'checkout/cart.html', {
                                            'cart_items': cart_items,
                                            'cart_subtotal': cart_subtotal,
                                            'all_products': all_products,
                                            })




def checkoutOne(request):
    form7 = CheckoutFormOne()


    if request.method == 'POST':
        form7 = CheckoutFormOne(request.POST)
        if form7.is_valid():
            cleaned_data = form7.cleaned_data
            o = Order(
                first_name = cleaned_data.get('first_name'),
                last_name = cleaned_data.get('last_name'),
                email = cleaned_data.get('email'),
                postal_code = cleaned_data.get('postal_code'),
                address = cleaned_data.get('address'),
                city = cleaned_data.get('city'),

            )
            o.save()

            all_items = cart.get_all_cart_items(request)
            for cart_item in all_items:
                li = LineItem(
                    product_id = cart_item.product_id,
                    price = cart_item.price,
                    quantity = cart_item.quantity,
                    order_id = o.id
                )

                li.save()
            # Clear car moved to after the payment has been completed or cancelled
            # cart.clear(request)

            request.session['order_id'] = o.id
            messages.add_message(request, messages.INFO, 'Order Placed!')
            return redirect( '/process_payment/')


    else:
        form = CheckoutFormOne()
        return render(request,'checkout/checkout_page.html',{'form7':form7})



# Payment Gateway, PalPal views


def process_payment(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    cart_items = cart.get_all_cart_items(request)
    cart_subtotal = cart.subtotal(request)
    host = request.get_host()
    # What you want the button to do.
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": '%.2f' % order.total_cost(),
        "item_name": 'Order {}'.format(order.id),
        "invoice": str(order.id),
        "currency_code": 'AUD',
        "notify_url": "http://{}{}".format(host, reverse('paypal-ipn')),
        "return_url": 'http://{}{}'.format(host, reverse('checkout:payment_done')),
        "cancel_return": 'http://{}{}'.format(host, reverse('checkout:payment_cancelled')),

    }

    # Create the instance.
    form_paypal = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'checkout/process_payment.html', {'order': order,
                                                             'form_paypal': form_paypal,
                                                             'cart_items': cart_items,
                                                             'cart_subtotal': cart_subtotal,
                                                             })




def payment_done(request):
    cart.clear(request)
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    lineitem = LineItem.objects.filter(order = order_id)

    return render(request, 'checkout/payment_done.html', {'order': order,
                                                          'lineitem': lineitem,
                                                          })



@csrf_exempt
def payment_cancelled(request):
    cart.clear(request)
    return render(request, 'checkout/payment_cancelled.html')


# HTML to PDF Views


def order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    lineitem = LineItem.objects.filter(order = order_id)

    html = render_to_string('checkout/pdf.html',{'order': order, 'lineitem': lineitem})
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'filename=\"order_{}.pdf"'.format(order_id)
    response['Content-Disposition'] = 'attachment;filename=\"order_{}.pdf"'.format(order_id)
    pdf = weasyprint.HTML(string=html).write_pdf(response,stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + '/css/pdf.css')])

    # pdf.save()

    return response
