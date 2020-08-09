from django.shortcuts import render
from django.http import HttpResponse

from .forms import ContactForm

# Formularz HTML
def form1(request):
    if request.method == "POST":
        print(request.POST)

    return render(request, 'forms/form1.html')


# Formularz Django
def form2(request):
    if request.method == "POST":
        form = ContactForm(request.POST) # bound
        if form.is_valid():
            print(form.cleaned_data)

    form = ContactForm() # unbound

    return render(request, 'forms/form2.html', {
        "form": form
    })