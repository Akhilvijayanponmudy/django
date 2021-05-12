from django.shortcuts import render, redirect
from .models import Book
from .forms import BookCreateForm


# Create your views here.

def book_create(request):
    form=BookCreateForm
    context={}
    context["form"]=form
    books=Book.objects.all()
    context["books"]=books
    if request.method=="POST":
        form=BookCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("")

    return render(request,"book/bookcreate.html",context)

def book_view(request):