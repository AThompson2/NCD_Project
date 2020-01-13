from django.urls import path, include
from django.conf.urls import url
from . import views



app_name = 'checkout'

urlpatterns = [
    path('checkout_form/', views.CheckoutForm.as_view(),name="checkout_form"),
    path('checkout_new/', views.CheckoutNew.as_view(),name="checkout_new"),
    path('checkout_thankyou/', views.CheckOutThankyou.as_view(),name="checkout_thankyou"),
    path('cart/', views.Cart.as_view(),name="cart"),
    path('checkout_index/', views.checkout_index, name="checkout_index"),
    path('product_detail/<int:product_id>/<slug:product_slug>/',views.show_product, name='product_detail'),
    path('show_cart/', views.show_cart, name='show_cart'),
    path('checkoutOne/', views.checkoutOne, name='checkoutOne'),
    path('process_payment/', views.process_payment, name='process_payment'),
    path('payment_done/', views.payment_done, name='payment_done'),
    path('payment_cancelled/', views.payment_cancelled, name='payment_cancelled'),
    path('order/<int:order_id>/',views.order_pdf,name='order_pdf'),
]
