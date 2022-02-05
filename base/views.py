from django.shortcuts import render, redirect
from .forms import *
from .models import *
# Create your views here.


def viewTasks(request):
    profile = request.user.profile
    tasks = profile.task_set.all()

    context = {'tasks': tasks}
    return render(request, 'base/list.html', context)


def createTask(request):
    profile = request.user.profile
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = profile
            form.save()
        return redirect('list')
    context = {'form': form}
    return render(request, 'base/add.html', context)


def updateTask(request, pk):
    profile = request.user.profile
    task = profile.task_set.get(id=pk)

    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('list')

    context = {'form': form}
    return render(request, 'base/update_task.html', context)


def deleteTask(request, pk):
    profile = request.user.profile
    task = profile.task_set.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('list')

    context = {'task': task}
    return render(request, 'base/delete.html', context)
