from django.shortcuts import render
from django.http import HttpResponse   
from .models import Task, Category, Priority 
from django.core.paginator import Paginator
# Create your views here.

def Home(request):
    search_query = request.GET.get("search-query", "")
    date_sort = request.GET.get("date-sort", "asc")
    status_filter = request.GET.getlist("status")
    category_filter = request.GET.getlist("category")
    priority_filter = request.GET.getlist("priority")
    
    categories = Category.objects.all()
    priorities = Priority.objects.all()
    tasks = Task.objects.all()
    
    if status_filter:
        tasks = tasks.filter(status__in=status_filter)
        
    if category_filter:
        tasks = tasks.filter(category__name__in=category_filter)
        
    if priority_filter:
        tasks = tasks.filter(priority__name__in=priority_filter)
    
    if date_sort == "asc":
        tasks = tasks.order_by('deadline')
    else:
        tasks = tasks.order_by('-deadline')
        
    if search_query:
        tasks = tasks.filter(title__contains=search_query)
    
    paginator = Paginator(tasks, 10) 
    page = request.GET.get('page')
    paginated_tasks = paginator.get_page(page)
    
    return render(request, 'home.html', {
        'tasks': paginated_tasks, 
        'categories': categories,
        'priorities': priorities})