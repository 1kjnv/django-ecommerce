from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from datetime import datetime


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, default="New User")
    last_name = models.CharField(max_length=50, default="New User")
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk":self.pk})

    class Meta:
        managed = True
        db_table = "user_profile"


class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(max_length=2000)
    color = models.CharField(max_length=50)
    category = models.CharField(max_length=255, default="Something")
    image = models.ImageField(upload_to='images/')
    quantity = models.IntegerField(default=1)
    
    created_at = models.DateTimeField(default=datetime.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("product_detail", kwarg={"pk":self.pk})

    def get_category(self):
        return self.category

    class Meta:
        managed = True
        db_table = 'item'

class Contact(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=2000)
    created_at = models.DateTimeField(default=datetime.now)

    class Meta:
        managed = True
        db_table = 'contact_details'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    totalprice = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(default = datetime.now)

    def __str__(self):
        return self.item
        
    class Meta:
        managed = True
        db_table = 'orders'