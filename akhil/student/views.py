from django.shortcuts import render

from django.http import HttpResponse



def Student_Login(request):
    return render(request,"student/student.html")

def Register(request):
    name=request.POST.get("sname")
    email=request.POST.get("mail")
    print(name,email)
    return render(request,"student/student.html")
