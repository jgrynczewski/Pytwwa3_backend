from django.shortcuts import render
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    t = Task.objects.all()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            task = Task(text=text)
            task.save()
    else:
        form = TaskForm()

    return render(request, 'tasks/task.html', {'tasks': t, "form": form})