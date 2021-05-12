from django.shortcuts import render

# Create your views here.
from .forms import BookCreateForm,BookUpdateForm
from django.shortcuts import render,redirect
from .models import Book
from .forms import UserRegForm,LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login

from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView,TemplateView
from django.urls import reverse_lazy

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
            print("book object saved")
            return redirect("create")
        else:
            form = BookCreateForm(request.POST)
            context["form"]=form
            return render(request, "book/bookedit.html", context)


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
    form=BookUpdateForm(instance=book)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=BookUpdateForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect("create")

    return render(request,"book/bookedit.html",context)


def registration(request):
    form=UserRegForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"book/login.html")
        else:
            form=UserRegForm(request.POST)
            context["form"]=form
            return render(request, "book/registration.html", context)

    return render(request,"book/registration.html",context)


def login_view(request):
    form=LoginForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                print("login success")

                login(request,user)

                return redirect("create")
            else:
                print("failed")
                return render(request, "book/login.html", context)

    return render(request,"book/login.html",context)




class Books(TemplateView):
    model = Book
    #context_object_name = "books"
    template_name = "book/bookcreate.html"
    context={}
    def get(self, request, *args, **kwargs):
        books=self.model.objects.all()
        self.context["books"]=books
        return render(request,self.template_name,self.context)


class BookCreate(TemplateView):
    model = Book
    form_class = BookCreateForm
    template_name = "book/bookcreate.html"
    context={}
    def get(self, request, *args, **kwargs):
        self.context["form"]=self.form_class()
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clslist")
        else:
            self.context["form"]=form
            return render(request,self.template_name,self.context)



class BookUpdateView(TemplateView):
    model = Book
    form_class = BookCreateForm
    template_name = "book/bookedit.html"
    context={}
    def get_object(self,id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        book=self.get_object(kwargs["pk"])
        form=self.form_class(instance=book)
        self.context["form"]=form
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        book=self.get_object(kwargs["pk"])
        form=self.form_class(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect("clslist")
        else:
            self.context["form"]=form
            return render(request,self.template_name,self.context)


class BookDetail(TemplateView):
    model = Book
    template_name = "book/bookdetail.html"
    context={}
    def get(self, request, *args, **kwargs):
        book=self.model.objects.get(id=kwargs["pk"])
        self.context["book"]=book
        return render(request,self.template_name,self.context)


class BookDelete(TemplateView):
    model = Book

    def get(self, request, *args, **kwargs):
        book=self.model.objects.get(id=kwargs["pk"])
        book.delete()
        return redirect("clslist")