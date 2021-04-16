from django import forms
from django.forms import ModelForm
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookCreateForm(ModelForm):
    class Meta:
        model=Book
        fields='__all__'
        widgets={
            "book_name":forms.TextInput(attrs={'class':"form-control"})
        }

    def clean(self):
        cleaned_data = super().clean()
        price=cleaned_data.get("price")

        if price<0:
            msg="invalid price pls provide valid price"
            self.add_error('price',msg)


class BookUpdateForm(ModelForm):
    class Meta:
        model=Book
        fields='__all__'



class UserRegForm(UserCreationForm):


    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1","password2"]


class LoginForm(forms.Form):
    username=forms.CharField(max_length=120)
    password=forms.CharField(widget=forms.PasswordInput)



