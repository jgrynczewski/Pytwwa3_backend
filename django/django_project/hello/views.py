from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
# Tworzenie widoków
def hello(request):
    return HttpResponse("Hello, world!")

# Przekazywanie danych z url-a do widoku
def hello2(request, name):
    return HttpResponse(f"Witaj, {name}")


# Szablony
def hello3(request):
    return render(request, 'hello/hello.html')


# Przekazywanie danych do szablonu
def hello4(request):
    name = "Ala"
    return render(request, 'hello/hello.html', {
        'name': name
    })
