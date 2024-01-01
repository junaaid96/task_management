from django.shortcuts import render, redirect
from .models import Task
from . import forms

# Create your views here.


def show_task(request):
    tasks = Task.objects.all()
    return render(request, "show_task.html", {"tasks": tasks})


def add_task(request):
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task')
    else:
        task_form = forms.TaskForm()
    return render(request, 'add_task.html', {'task_form': task_form})

def edit_task(request, id):
    task = Task.objects.get(pk=id)
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task')
    else:
        task_form = forms.TaskForm(instance=task)
    return render(request, 'add_task.html', {'task_form': task_form})

def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('show_task')
