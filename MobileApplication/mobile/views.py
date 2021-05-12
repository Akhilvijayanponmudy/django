from django.shortcuts import render,redirect
from mobile.forms import BrandCreateForm,MobileCreateForm
from .models import Brands, Mobile, Orders
from .forms import UserRegForm,OrderForm
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
# Create your views here.

def admin_permission_required(func):
    def wrapper(request):
        if not request.user.is_superuser:
            return redirect("errorpage")
        else:
            return func(request)
    return wrapper

@admin_permission_required
def brand_view(request):

    brands=Brands.objects.all()
    form=BrandCreateForm()
    context={}
    context["brands"]=brands
    context["form"]=form
    if request.method=="POST":
        form=BrandCreateForm(request.POST)
        if form.is_valid():
            form.save()
            print("Saved")
            return redirect("brandview")
    return render(request,"mobile/brandcreate.html",context)



def errorpg(request):
    return render(request,"mobile/errorpage.html")


def create_mobile(request):
    form=MobileCreateForm
    context={}
    context["form"]=form
    if request.method=="POST":
        form=MobileCreateForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            print("saved")
            return redirect("createmobile")
    return render(request,"mobile/mobilecreate.html",context)


def brand_del(request):
    brand=Brands.objects.get(id=id)
    brand.delete()
    return redirect("brandview")




def list_mobiles(request):
    mobiles=Mobile.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request,"mobile/listmobiles.html",context)


def mobile_detail(request,id):
    mobile=Mobile.objects.get(id=id)
    context={}
    context["mobile"]=mobile
    return render(request,"mobile/mobiledetail.html",context)


def user_registration(request):
    form=UserRegForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("userlogin")
        else:
            form=UserRegForm(request.POST)
            context["form"]=form
            return render(request, "mobile/userreg.html", context)
    return render(request,"mobile/userreg.html",context)


def user_login(request):
    if request.method=="POST":
        username=request.POST.get("uname")
        password=request.POST.get("pwd")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect("listmobiles")
        else:
            return render(request,"mobile/login.html")
    return render(request,"mobile/login.html")


def user_logout(request):
    logout(request)
    return redirect("userlogin")


def order(request,id):
    product=Mobile.objects.get(id=id)
    form = OrderForm(initial={'user': request.user,'product':product})
    context = {}
    context["form"] = form

    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            print("saved")
            return redirect("cart")
        else:
            form=OrderForm(request.POST)
            context["form"]=form
            return render(request, "mobile/order.html", context)
    return render(request,"mobile/order.html",context)


def cart_view(request):
    userna=request.user
    carts=Orders.objects.filter(user=userna)
    print(carts)
    context={}
    context["carts"]=carts
    return render(request,"mobile/mobcart.html",context)
