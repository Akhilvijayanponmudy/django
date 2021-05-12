from django.forms import ModelForm, forms
from mobile.models import Brands,Mobile,Orders
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BrandCreateForm(ModelForm):
    class Meta:
        model=Brands
        fields="__all__"


class MobileCreateForm(ModelForm):
    class Meta:
        model=Mobile
        fields="__all__"


class UserRegForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password1','password2']



class OrderForm(ModelForm):
    class Meta:
        model=Orders
        fields="__all__"
