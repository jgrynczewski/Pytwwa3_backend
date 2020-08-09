from django.shortcuts import render


def form1(request):
    if request.method == "POST":
        print(request.POST)

    return render(request, 'forms/form1.html')