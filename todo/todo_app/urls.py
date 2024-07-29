from django.urls import path
from . import views
urlpatterns = [
path("",views.home,name="home"),
path("todo/",views.todo,name="todo"),
path("add_todo",views.add_todo,name="add_todo"),
path("delete_todo/<int:task_id>",views.delete_todo,name="delete_todo"),
path("update_todo/<int:task_id>",views.update_todo,name="update_todo"),
path("mark_complete/<int:task_id>",views.mark_complete,name="mark_complete"),
]