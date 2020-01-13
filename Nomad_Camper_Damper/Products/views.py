from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView,View,DetailView,ListView
from Products.models import ProductDB
from . import models
from . import views
# Create your views here.


class Products_list(ListView):
    context_object_name ='product_list'
    model = models.ProductDB
    template_name = 'Products/products_list.html'

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['injectme'] = "Basic Injection!"
        return context


class Individual_product_page(DetailView):
    context_object_name ='Individual_product'
    model = models.ProductDB
    template_name = 'Products/individual_product_page.html'
