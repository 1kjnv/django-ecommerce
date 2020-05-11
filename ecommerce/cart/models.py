from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from backend.models import Item
from django.db.models import F, Sum
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(default = datetime.now)

    def __str__(self):
        return self.user.username + "'s cart"
    
    class Meta:
        managed = True
        db_table = 'cart'


class CartItem(models.Model):
    product = models.ForeignKey(Item, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(default = 0.00, max_digits = 10, decimal_places = 2)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=100, decimal_places=2, default=0)

    def get_price(self):
        return self.quantity * self.price

    def __str__(self):
        return self.product.name

    class Meta:
        managed = True
        db_table = 'cart_item'
        