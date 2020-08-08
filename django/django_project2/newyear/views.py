from datetime import datetime

from django.shortcuts import render

# Create your views here.

def index(request):
    now = datetime.now()

    # Teranary operator
    result  = True if (now.month==8 and now.day==8) else False

    return render(request, 'newyear/index.html', {
        "result":result
    })