from django.shortcuts import render, redirect
from .models import CategoryModel
from .forms import CategoryForm

# Create your views here.


def add_category(request):
    if request.method == "POST":
        category_from = CategoryForm(request.POST)
        if category_from.is_valid():
            print("category", category_from.cleaned_data)
            category_from.save()
            return redirect("home")
    else:
        category_from = CategoryForm()
    return render(request, "add_category.html", {"form": category_from})


def edit_category(request, id):
    category = CategoryModel.objects.get(pk=id)
    category_from = CategoryForm(instance=category)
    if request.method == "POST":
        category_form = CategoryForm(request.POST, instance=category)
        category_form.save()
        return redirect("home")

    return render(request, "add_category.html", {"form": category_from})


def delete_category(request, id):
    category = CategoryModel.objects.get(pk=id)
    category.delete()
    return redirect("home")
