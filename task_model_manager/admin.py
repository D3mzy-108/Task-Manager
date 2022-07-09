from django.contrib import admin

from task_model_manager.models import Note, Project, Task


# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass
