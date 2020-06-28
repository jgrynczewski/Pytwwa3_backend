from django.shortcuts import render
from .models import Task

# Create your views here.
def index(request):
    t = Task.objects.all()
    return render(request, 'tasks/task.html', {'tasks': t})