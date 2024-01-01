from django.urls import path
from .views import show_task, add_task, edit_task, delete_task

urlpatterns = [
    path("", show_task, name="show_task"),
    path("add/", add_task, name="add_task"),
    path("edit/<int:id>/", edit_task, name="edit_task"),
    path("delete/<int:id>/", delete_task, name="delete_task"),
]
