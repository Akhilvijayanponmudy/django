from django import forms
from django.forms import ModelForm
from bill.models import Order,Purchase
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class OrderCreateForm(ModelForm):
    class Meta:
        model=Order
        fields=["bill_number","customer_name","phone_number"]

class OrderLineForm(forms.Form):
    bill_number=forms.CharField()
    products=Purchase.objects.all().values_list('product__product_name')
    result=[(itemtuple[0],itemtuple[0]) for itemtuple in products]

    product_name=forms.ChoiceField(choices=result)
    product_qty=forms.IntegerField()

class UserRegistraionForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','username','email','password1','password2']