from django.shortcuts import render

from . import forms
# Create your views here.

def register(request):
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.RegisterForm()
    return render(request, "registration/register.html", {"form": form})