from django.shortcuts import render
from django.http import HttpResponse   
from .models import Task
# Create your views here.

def Home(request):
    search_query = request.GET.get("search-query", "")
    date_filter = request.GET.get("date-filter", "asc")
    
    tasks = Task.objects.all()
    
    if date_filter == 'asc':
        tasks = tasks.order_by('deadline')
    else:
        tasks = tasks.order_by('-deadline')
        
    if search_query:
        tasks = tasks.filter(title__contains=search_query)
    
    return render(request, 'home.html', {'tasks': tasks, 'date_filter': date_filter})