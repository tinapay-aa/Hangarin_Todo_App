from django import forms 
from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'status', 'category', 'priority']
        widgets = {
            'description': forms.Textarea(),
            'deadline': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local'
                }
            )
        }