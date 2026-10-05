from django.shortcuts import render
from django.http import HttpResponse   
from .models import Task, Category, Priority 
from django.core.paginator import Paginator
# Create your views here.

def Home(request):
    search_query = request.GET.get("search-query", "")
    
    categories = Category.objects.all()
    priorities = Priority.objects.all()
    tasks = Task.objects.all()
    
    if search_query:
        tasks = tasks.filter(title__contains=search_query)
        
    paginator = Paginator(tasks, 10) 
    page = request.GET.get('page')
    paginated_tasks = paginator.get_page(page)
    
    
    return render(request, 'home.html', {
        'tasks': paginated_tasks, 
        'categories': categories,
        'priorities': priorities})