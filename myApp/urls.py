from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('hello/<str:username>', views.hello, name="hello"),
    path('projects/', views.projects, name="projects"), 
    path('projects_detail/<int:id>', views.projects_detail, name="projects_detail"),
    path('tasks/', views.tasks, name="tasks"),
    path('create_task/', views.create_task, name="create_tasks"),
    path('create_new_projects/', views.create_projects, name="create_projects")

    
]
