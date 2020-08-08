from django.shortcuts import render
from django.http import HttpResponse

tasks = []

# Create your views here.
def index(request):
    return render(request, 'tasks_db/index.html', {
        "tasks": tasks
    })


def register(request):
    t = request.GET['task']
    tasks.append(t)
    return render(request, 'tasks_db/index.html', {
        "tasks": tasks
    })