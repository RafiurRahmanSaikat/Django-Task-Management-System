from django.shortcuts import render
from task.models import TaskModel

# Create your views here.


def home(request):
    data = TaskModel.objects.all()
    # print("Data", data)
    for task in data:
        print("Task", task.categories.all())
    return render(request, "home.html", {"data": data})
