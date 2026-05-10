from django.contrib import messages
from django.db import DatabaseError
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods, require_POST

from .models import Task


def index(request):
    tasks = Task.objects.filter(completed=False)
    total_count = Task.objects.count()
    completed_count = Task.objects.filter(completed=True).count()
    remaining_count = total_count - completed_count

    context = {
        "tasks": tasks,
        "total_count": total_count,
        "completed_count": completed_count,
        "remaining_count": remaining_count,
    }
    return render(request, "tasks/index.html", context)


def all_tasks(request):
    tasks = Task.objects.all()
    total_count = tasks.count()
    completed_count = tasks.filter(completed=True).count()
    remaining_count = total_count - completed_count

    context = {
        "tasks": tasks,
        "total_count": total_count,
        "completed_count": completed_count,
        "remaining_count": remaining_count,
    }
    return render(request, "tasks/all_tasks.html", context)


@require_POST
def add_task(request):
    title = request.POST.get("title", "").strip()
    if not title:
        messages.error(request, "Please enter a task title.")
        return redirect("tasks:index")

    try:
        Task.objects.create(title=title)
        messages.success(request, "Task added.")
    except DatabaseError:
        messages.error(request, "Could not add task. Please try again.")

    return redirect("tasks:index")


@require_POST
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    try:
        task.completed = not task.completed
        task.save(update_fields=["completed"])
    except DatabaseError:
        messages.error(request, "Could not update task. Please try again.")

    return redirect("tasks:index")


@require_POST
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    try:
        task.delete()
    except DatabaseError:
        messages.error(request, "Could not delete task. Please try again.")

    return redirect("tasks:all")


@require_http_methods(["GET", "POST"])
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        if not title:
            messages.error(request, "Please enter a task title.")
            return redirect("tasks:edit", task_id=task.id)

        try:
            task.title = title
            task.save(update_fields=["title"])
            messages.success(request, "Task updated.")
        except DatabaseError:
            messages.error(request, "Could not update task. Please try again.")

        return redirect("tasks:all")

    return render(request, "tasks/edit.html", {"task": task})
