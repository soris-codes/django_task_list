from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'complete']

def todo_create(request, template_name='todos/todo_form.html'):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('todo_list')
    return render(request, template_name, {'form':form, 'new_or_edit': 'New'})

def todo_list(request, template_name='todos/todo_list.html'):
    todos = Task.objects.all()
    data = {'object_list': todos}
    return render(request, template_name, data)

def todo_view(request, pk, template_name='todos/todo_detail.html'):
    todo = get_object_or_404(Task, pk=pk)
    data = {'object': todo}
    return render(request, template_name, data)

def todo_update(request, pk, template_name='todos/todo_form.html'):
    todo = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=todo)
    if form.is_valid():
      form.save()
      return redirect('todo_list')
    return render(request, template_name, {'form': form, 'new_or_edit': 'Edit'})

def todo_delete(request, pk, template_name='todos/todo_confirm_delete.html'):
    todo = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
      todo.delete()
      return redirect ('todo_list')
    return render(request, template_name, {'object': todo})



