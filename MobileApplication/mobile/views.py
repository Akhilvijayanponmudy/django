from django.shortcuts import render,redirect
from mobile.forms import BrandCreateForm,MobileCreateForm
from .models import Brands,Mobile
# Create your views here.


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


def list_mobiles(request):
    mobiles=Mobile.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request,"mobile/listmobiles.html",context)

