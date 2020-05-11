from .models import *
from cart.models import Item
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class EditProfileForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name','email',)


class EditProduct(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ('name','price','description','color','category','image','quantity',)