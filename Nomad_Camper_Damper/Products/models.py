from django.db import models


# Create your models here.


class ProductDB(models.Model):
    product_name = models.CharField(max_length=200,unique=True)
    product_pic = models.ImageField(upload_to= 'Nomad_Camper_Damper/static/images')
    product_info = models.TextField()
    product_price = models.DecimalField(max_digits=7, decimal_places=2)
    slug = models.SlugField(blank=True,default=None)


    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse("Products:individual_product",kwargs={'pk':self.pk})
