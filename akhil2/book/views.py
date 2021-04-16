from django.shortcuts import render
from .models import Book
from .forms import BookCreateForm


# Create your views here.

def book_create(request):
    form=BookCreateForm
    context={}
    context["form"]=form
    books=Book.objects.all()
    context["books"]=books
    return render(request,"book/bookcreate.html",context)