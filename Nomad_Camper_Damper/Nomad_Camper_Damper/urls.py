"""Nomad_Camper_Damper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render, redirect


urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('',views.HomePage.as_view(),name="home"),
    path('about_us/',views.AboutUs.as_view(),name="about_us"),
    path('contact_us/',views.ContactUs.as_view(),name="contact_us"),
    path('Products/',include("Products.urls", namespace="Products")),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('',include("checkout.urls", namespace="checkout")),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)