from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    tasks = Task.objects.all()
    paginator = Paginator(tasks, 6)
    page_number = request.GET.get('page')
    tasks = paginator.get_page(page_number)

    context = {'tasks': tasks}
    return render(request, "task/index.html", context)

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    context = {'task': task}
    return render(request, "task/task_detail.html", context)

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Votre demande a été ajoute")
            return redirect('home')
    else:
        form = TaskForm()
    context = {'form': form}
    return render(request, "task/task_add.html", context)

@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return render(request, "task/confirm_delete.html")

@login_required
def task_update(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        messages.success(request, f"Votre demande a été ajoute")
        return redirect('home')
    context = {'form': form}
    return render(request, "task/task_update.html", context)