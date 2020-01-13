from django.contrib import admin
from .models import CartItem, Order, LineItem
from django.utils.safestring import mark_safe
from django.shortcuts import render, HttpResponse, redirect, \
    get_object_or_404, reverse
# Register your models here.









class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_pdf', 'id', 'first_name', 'last_name', 'email','postal_code', 'address', 'city', 'date', 'paid']

    def order_pdf(self,obj):
        return mark_safe('<a href="{}">Invoice</a>'.format(reverse('checkout:order_pdf', args=[obj.id])))
    order_pdf.short_description = 'Invoice'


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'quantity', 'product']


class LineItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'quantity', 'date_added', 'order']



admin.site.register(Order, OrderAdmin)
admin.site.register(LineItem, LineItemAdmin)
admin.site.register(CartItem, OrderItemAdmin)
