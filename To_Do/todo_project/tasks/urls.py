from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    path("all/", views.all_tasks, name="all"),
    path("add/", views.add_task, name="add"),
    path("toggle/<int:task_id>/", views.toggle_task, name="toggle"),
    path("delete/<int:task_id>/", views.delete_task, name="delete"),
    path("edit/<int:task_id>/", views.edit_task, name="edit"),
]
