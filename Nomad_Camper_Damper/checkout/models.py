from django.db import models
from Products.models import ProductDB

# Create your models here.



class CartItem(models.Model):
    quantity = models.IntegerField()
    cart_id = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    product = models.ForeignKey(ProductDB, on_delete=models.PROTECT)


    def __str__(self):
        return self.cart_id


    def update_quantity(self, quantity):
        self.quantity = self.quantity + quantity
        self.save()


    def total_cost(self):
            return self.quantity * self.price



class Order(models.Model):
    first_name = models.CharField(max_length=191,default='')
    last_name = models.CharField(max_length=191)
    email = models.EmailField()
    postal_code = models.IntegerField()
    address = models.CharField(max_length=191)
    city = models.CharField(max_length=191)
    date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    # Invoice_pdf = models.FileField(null=True, blank=True, upload_to='static')

    def __str__(self):
        return "{}:{}".format(self.id, self.email)

    def total_cost(self):
        return sum([ li.cost() for li in self.lineitem_set.all() ] )

class LineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductDB, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}:{}".format(self.product.product_name, self.id)

    def cost(self):
        return self.price * self.quantity
