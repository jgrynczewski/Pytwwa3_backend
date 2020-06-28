from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse("Witaj świecie!")


def drugi(request):
    msg = "<!DOCTYPE html><html><head><title>Drugi widok</title></head><body>To jest drugi widok <p>Nowa linia</p></body></html>"
    return HttpResponse(msg)


def trzeci(request):
    return render(request, 'hello/trzeci.html')