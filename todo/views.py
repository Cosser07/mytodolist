from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm


# Create your views here.

#อ่านและเพิ่มงาน
def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    return render(request, 'todolist/task_list.html', {'tasks': tasks, 'form': form})

#อัปเดตงาน
def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todolist/task_update.html', {'form': form})

#ลบงาน
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

def task_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')