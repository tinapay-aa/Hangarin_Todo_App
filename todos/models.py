from django.db import models

# Create your models here
class TaskStatus(models.TextChoices):
    IN_PROGRESS = 'in_progress', 'In progress'
    COMPLETE = 'complete', 'Complete'
    EXPIRED = 'expired', 'Expired'
    
class Category(models.Model):
    name = models.CharField(max_length=50)

class Priority(models.Model):
    name  = models.CharField(max_length=50)
    
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    deadline = models.models.DateTimeField(_("Deadline"), auto_now=False, auto_now_add=False)
    status = models.CharField(
        max_length=20,
        choices=TaskStatus.choices,
        default=TaskStatus.IN_PROGRESS
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True
    )
    priority = models.ForeignKey(
        Priority,
        on_delete = models.SET_NULL,
        null = True
    )

class Note(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE
    )
    content = models.CharField(max_length=200)

class SubTask(models.Model):
    parent_task = models.ForeignKey(
        Task, 
        on_delete = models.CASCADE
    )