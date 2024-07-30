from django.shortcuts import render,redirect
from .models import Todo
from datetime import datetime

def home(request):
    return render(request,"index.html")

def todo(request):
    task=Todo.objects.filter(is_complete=False)
    complete_task=Todo.objects.filter(is_complete=True)

    parameter={
        "todos":task,
        "complete_task":complete_task
    }
    return render(request,"todo.html",parameter)

def add_todo(request):
    if request.method=="POST":
        task=request.POST.get("task")
        created_at=datetime.today()
        naya_todo=Todo(task=task,created_at=created_at)
        naya_todo.save()

        return redirect("todo")

    return render(request,"add_todo.html")

def delete_todo(request,task_id):
    task=Todo.objects.get(id=task_id)
    task.delete()

    return redirect("todo")

def update_todo(request,task_id):
    todo=Todo.objects.get(id=task_id)

    if request.method=="POST":
        update_task=request.POST.get("update_task")
        created_at=datetime.today()

        todo.task=update_task
        todo.created_at=created_at
        todo.save()
        
        return redirect("todo")


    parameter={
        "todo":todo
    }

    return render(request,"update_todo.html",parameter)


def mark_complete(request,task_id):
    todo=Todo.objects.get(id=task_id)
    todo.is_complete=True
    todo.save()
    
    return redirect("todo")