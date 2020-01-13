from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'


class AboutUs(TemplateView):
    template_name = 'about_us.html'

class ContactUs(TemplateView):
    template_name = 'contact_us.html'
