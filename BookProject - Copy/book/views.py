from django.shortcuts import render

# Create your views here.
from .forms import BookCreateForm
from django.shortcuts import render,redirect
from.models import Book


def book_create(request):
    form=BookCreateForm()
    context={}
    context["form"]=form
    books=Book.objects.all()
    context["books"]=books
    if request.method=="POST":


        form=BookCreateForm(request.POST)
        if form.is_valid():
            book_name=form.cleaned_data.get("book_name")
            author=form.cleaned_data.get("author")
            price=form.cleaned_data.get("price")
            pages=form.cleaned_data.get("pages")
            category=form.cleaned_data.get("category")


            book=Book(book_name=book_name,author=author,price=price,pages=pages,category=category)
            book.save()
            print("book saved")
            return redirect("create")
    return render(request,"book/bookcreate.html",context)

def book_delete(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect("create")

def book_view(request,id):
    book=Book.objects.get(id=id)
    context={}
    context["book"]=book
    return render(request,"book/bookdetail.html",context)

def book_update(request,pk):
    book=Book.objects.get(id=pk)
    form=BookCreateForm(instance=book)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=BookCreateForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect("create")

    return render(request,"book/bookedit.html",context)

