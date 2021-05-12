
from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from .views import OrderCreateViewe,OrderLineView,BillGenerate,Search_View,UserRegistrationView,UserLoginView,user_logout

urlpatterns = [
    path("",lambda request:render(request,"bill/index.html")),
    path("createorder",OrderCreateViewe.as_view(),name="createorder"),
    path("orderLine/<str:bill_num>",OrderLineView.as_view(),name="orderline"),
    path("generatebill/<str:billnum>",BillGenerate.as_view(),name="completeorder"),
    path("search",Search_View,name="search"),
    path("error",lambda request:render(request,"bill/error.html"),name="error"),
    path("register",UserRegistrationView.as_view(),name="registration"),
    path("login",UserLoginView.as_view(),name="login"),
    path("logout",user_logout,name="logout")

]
