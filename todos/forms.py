from django import forms 
from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'status', 'category', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input'}),
            'deadline': forms.DateTimeInput(attrs={
                'class': 'form-input',
                'type': 'datetime-local'
            }),
            'status': forms.Select(attrs={'class': 'form-input'}),
            'category': forms.Select(attrs={'class': 'form-input'}),
            'priority': forms.Select(attrs={'class': 'form-input'}),
            }