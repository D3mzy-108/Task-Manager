from django.db import models


# Create your models here.
class Project(models.Model):
    project = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.project


class Task(models.Model):
    task = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.BooleanField(default=False)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="tasks", blank=True, null=True)

    def __str__(self):
        return f"{self.task} -> {self.status}"


class Note(models.Model):
    note = models.CharField(max_length=300)
    is_done = models.BooleanField(default=False)
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.note
