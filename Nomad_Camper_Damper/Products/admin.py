from django.contrib import admin
from Products.models import ProductDB
# Register your models here.






class ProductDBAdmin(admin.ModelAdmin):
    list_display =['id', 'product_name', 'product_price']


admin.site.register(ProductDB, ProductDBAdmin)
