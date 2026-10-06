from django.db import models

# Create your models here
class TaskStatus(models.TextChoices):
    PENDING = 'Pending', 'pending'
    IN_PROGRESS = 'In Progress', 'in_progress'
    COMPLETE = 'Completed', 'completed'
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Priority(models.Model):
    name  = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name = 'Priority'
        verbose_name_plural = 'Priorities'
    
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    deadline = models.DateTimeField(("Deadline"), auto_now=False, auto_now_add=False)
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
    
    def __str__(self):
        return self.title

class Note(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="notes"
    )
    content = models.CharField(max_length=200)
    
    def __str__(self):
        return self.content

class SubTask(models.Model):
    parent_task = models.ForeignKey(
        Task, 
        on_delete = models.CASCADE,
        related_name="subtasks"
    )
    title = models.CharField(max_length=50, default="Untitled")
    status = models.CharField(
        max_length=20,
        choices=TaskStatus.choices,
        default=TaskStatus.IN_PROGRESS
    )
    
    def __str__(self):
        return self.title