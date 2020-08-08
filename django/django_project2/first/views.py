from django.shortcuts import render
from django.http import HttpResponse


# Widoki
def hello(request):
    return HttpResponse("Hello, world!")


# Konwertery (str, int, uid, url, slug)
def test(request, num):
    return HttpResponse(f"{num*2}")


# Szablony
def read(request, foo):
    return render(request, 'first/read.html', {
        "foo":foo,
    })