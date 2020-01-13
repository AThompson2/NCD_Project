from django import forms
from checkout.models import CartItem, Order, LineItem
from Products.models import ProductDB



class CartForm(forms.Form):
    quantity = forms.IntegerField(initial='1')
    product_id = forms.IntegerField(widget = forms.HiddenInput(), required = False)

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(CartForm, self).__init__(*args, **kwargs)







class CheckoutFormOne(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('paid',)

        widgets = {
            'address': forms.Textarea(attrs={'row': 5, 'col': 8}),

        }
