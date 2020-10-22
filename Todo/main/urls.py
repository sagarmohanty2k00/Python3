from . import views
from django.urls import path

urlpatterns = [
    path('', views.todoView),
    path('add_todo/', views.add_todo),
    path('delete_todo/<int:todo_id>/', views.delete_todo),
]