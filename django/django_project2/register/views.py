from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.http import HttpResponse

from . import forms
# Create your views here.

def register(request):
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse("hello"))
    else:
        form = forms.RegisterForm()
    return render(request, "registration/register.html", {"form": form})

def hello(request):
    return HttpResponse("Rejestracja przebiegła pomyślnie")

def hello_login(request):
    return render(request, "registration/hello.html")
