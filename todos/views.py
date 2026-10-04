from django.shortcuts import render
from django.http import HttpResponse   
from .models import Task, Category, Priority 
# Create your views here.

def Home(request):
    search_query = request.GET.get("search-query", "")
    
    categories = Category.objects.all()
    priorities = Priority.objects.all()
    tasks = Task.objects.all()
    
    if search_query:
        tasks = tasks.filter(title__contains=search_query)
    
    return render(request, 'home.html', {
        'tasks': tasks, 
        'categories': categories,
        'priorities': priorities})