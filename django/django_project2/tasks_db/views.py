from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from .models import Task


# Create your views here.
def index(request):
    tasks = Task.objects.all()

    return render(request, 'tasks_db/index.html', {
        "tasks": tasks
    })


@require_http_methods("[POST]")
def register(request):
    t = request.POST['task']

    # C (CREATE - insert) z CRUD
    task = Task(text=t)
    task.save()

    # R (READ - select) z CRUD
    tasks = Task.objects.all()
    # objects - menadżer zapytań
    # metody all(), first(), filter(), ... tego obiektu zwracają obiekt klasy QuerySet

    return render(request, 'tasks_db/index.html', {
        "tasks": tasks
    })


@require_http_methods(["GET", "POST"])
def update(request, task_id):

    # t = Task.objects.filter(id=task_id).first()
    # t = Task.objects.get(id=task_id)
    t = Task.objects.get(pk=task_id)

    if request.method == "GET":
        return render(request, 'tasks_db/update.html', {
            "task":t,
        })

    else:
        # U (Update) z CRUD
        t.text = request.POST.get("task")
        t.save()

        return redirect("tasks_db:index")