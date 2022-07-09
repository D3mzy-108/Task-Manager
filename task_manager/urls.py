from django.urls import path

from task_manager.views import *

urlpatterns = [
    path('', home, name="home"),
    path('today/', today, name="today"),
    path('tomorrow/', tomorrow, name="tomorrow"),
    path('overdue/', overdue, name="overdue"),
    path('projects/', project, name="projects"),
    path('project_tasks<int:id>/', project_tasks, name="project_tasks"),
    path('search/', search, name="search"),
    path('notes<int:id>/', notes, name="notes"),
    path('update_note<int:id>/', update_notes, name="update_notes"),
    path('delete_task<int:id>/', delete_task, name="delete_task"),
    path('delete_project<int:id>/', delete_project, name="delete_project"),
    path('completed_task<int:id>/', update_task, name="update_task"),
    path('add_project/', add_project, name="add_project"),
    path('add_task/', add_task, name="add_task"),
    path('add_task<int:id>/', add_task2, name="add_task2"),
    path('add_note/', add_note, name="add_note"),
    path('add_note<int:id>/', add_note2, name="add_note2"),
    path('edit_task<int:id>/', edit_task, name="edit_task"),
    path('edit_project<int:id>/', edit_project, name="edit_project"),
]
