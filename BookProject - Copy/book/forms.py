from django import forms
from django.forms import ModelForm
from .models import Book

class BookCreateForm(forms.Form):
    book_name=forms.CharField(max_length=120)
    author=forms.CharField(max_length=180)
    price=forms.IntegerField()
    pages=forms.IntegerField()
    category=forms.CharField(max_length=120)



