from django.forms import ModelForm
from .models import Book
from django import forms


class BookCreateForm(ModelForm):
    class Meta:
        model=Book
        fields='__all__'



