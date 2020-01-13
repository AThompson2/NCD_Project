from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'Products'

urlpatterns = [
     path('',views.Products_list.as_view(),name="list"),
     path('<int:pk>/',views.Individual_product_page.as_view(),name="individual_product"),
     path('checkout/',include("checkout.urls", namespace="checkout")),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
