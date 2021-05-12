from django import forms
from django.shortcuts import render, redirect
from bill.forms import OrderCreateForm,OrderLineForm,UserRegistraionForm
from django.views.generic import TemplateView
from bill.models import Order,OrderLines,Purchase,Product
from django.db.models import Sum
from .filters import OrderFilter
from bill.decorators import admin_only
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from bill.authentication import EmailAuthBackend
from django.contrib.auth import login, logout


# Create your views here.

@method_decorator(admin_only,name='dispatch')
class OrderCreateViewe(TemplateView):
    model=Order
    form_class=OrderCreateForm
    template_name = "bill/ordercreate.html"
    context={}
    def get(self, request, *args, **kwargs):
        print(request.user)
        order=self.model.objects.last()
        if order:
            last_billnum=order.bill_number
            lst=int(last_billnum.split("-")[1])+1
            bill_number="lulu-"+str(lst)


        else:
            bill_number="lulu-1000"

        form = self.form_class(initial={"bill_number":bill_number})
        self.context["form"] = form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            bill_number=form.cleaned_data.get("bill_number")
            form.save()
            return redirect("orderline",bill_num=bill_number)

@method_decorator(admin_only,name='dispatch')
class OrderLineView(TemplateView):
    model=OrderLines
    form_class=OrderLineForm
    template_name = "bill/orderline.html"
    context={}

    def get(self, request, *args, **kwargs):
        bill_number=kwargs.get("bill_num")

        form=self.form_class(initial={"bill_number":bill_number})
        self.context["form"]=form
        queryset = self.model.objects.filter(bill_number__bill_number=bill_number)
        total=OrderLines.objects.filter(bill_number__bill_number=bill_number).aggregate(Sum('amount'))

        ctotal=total["amount__sum"]
        self.context["items"]=queryset
        self.context["total"]=ctotal
        self.context["bill_number"]=bill_number
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            bill_number=form.cleaned_data.get("bill_number")
            bill=Order.objects.get(bill_number=bill_number) #bill number ulla object kittan
            product_name=form.cleaned_data.get("product_name")
            prdt=Product.objects.get(product_name=product_name)
            qty=form.cleaned_data.get("product_qty")
            product=Purchase.objects.get(product__product_name=product_name)
            amount=product.selling_price*qty
            orderline=self.model(bill_number=bill,product=prdt,product_qty=qty,amount=amount)
            orderline.save()
            print("order saved")
            return redirect("orderline",bill_num=bill_number)


@method_decorator(admin_only,name='dispatch')
class BillGenerate(TemplateView):
    def get(self, request, *args, **kwargs):
        bill_number=kwargs.get("billnum")
        total=OrderLines.objects.filter(bill_number__bill_number=bill_number).aggregate(Sum('amount'))
        grandtotal=total["amount__sum"]
        order=Order.objects.get(bill_number=bill_number)
        order.bill_total=grandtotal
        order.save()
        queryset=OrderLines.objects.filter(bill_number__bill_number=bill_number)
        context={}
        context["items"]=queryset
        context["gtotal"]=grandtotal
        return render(request,"bill/customerBill.html",context)



def Search_View(request):
    orders=Order.objects.all()
    context={}
    orderfilter=OrderFilter(request.GET,queryset=orders)
    context["filter"]=orderfilter
    return render(request,"bill/search.html",context)

class UserRegistrationView(TemplateView):
    form_class=UserRegistraionForm
    model=User
    template_name = "bill/userregistration.html"
    def get(self, request, *args, **kwargs):
        form=self.form_class()
        context={}
        context["form"]=form
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.post)
        if form.is_valid():
            form.save()
            return redirect("login")


class LoginForm(forms.Form):
    email=forms.CharField()
    password=forms.CharField()


class UserLoginView(TemplateView):
    form_class=LoginForm
    def get(self, request, *args, **kwargs):
        context={}
        context["form"]=self.form_class()
        return render(request,"bill/userlogin.html",context)

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get("email")
            password=form.cleaned_data.get("password")
            obj=EmailAuthBackend()
            user=obj.authenticate(request,username=email,password=password)
            if user:
                login(request,user)
                return redirect("createorder")


def user_logout(request):
    logout(request)
    return redirect("login")





