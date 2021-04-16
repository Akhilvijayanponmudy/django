from django.http import HttpResponse



def index(request):
    return HttpResponse("<h1>Welcome to django<h1>")


def register(request):
    return HttpResponse("<h1>Welcome to Registration<h1>")


def login(request):
    return HttpResponse("<h1>Welcome to login<h1>")