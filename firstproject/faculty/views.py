from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from faculty.forms import StudentRegistrationForm


def registration(request):
    form=StudentRegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=StudentRegistrationForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get("name")
            email=form.cleaned_data.get("email")
            phone_number=form.cleaned_data.get("phone")
            print(name,"=>",email,"=>",phone_number)
            return render(request,"faculty/studentregistration.html", context)


    return render(request,"faculty/studentregistration.html",context)