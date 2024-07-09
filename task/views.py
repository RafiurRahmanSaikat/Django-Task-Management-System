from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import TaskModel

# Create your views here.


def add_task(request):
    if request.method == "POST":
        task_from = TaskForm(request.POST)
        if task_from.is_valid():
            print("Task", task_from.cleaned_data)
            task_from.save()
            return redirect("home")
    else:
        task_from = TaskForm()
    return render(request, "add_task.html", {"form": task_from})


def edit_task(request, id):
    task = TaskModel.objects.get(pk=id)
    task_from = TaskForm(instance=task)
    if request.method == "POST":
        task_form = TaskForm(request.POST, instance=task)
        task_form.save()
        return redirect("home")

    return render(request, "add_task.html", {"form": task_from})


def delete_task(request, id):
    task = TaskModel.objects.get(pk=id)
    task.delete()
    return redirect("home")
