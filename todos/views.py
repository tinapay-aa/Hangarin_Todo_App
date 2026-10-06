from django.shortcuts import render
from django.http import HttpResponse   
from .models import Task, Category, Priority, SubTask, Note
from .forms import TaskForm
from django.core.paginator import Paginator
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
# Create your views here.

def Home(request):
    search_query = request.GET.get("search-query", "")
    date_sort = request.GET.get("date-sort", "asc")
    status_filter = request.GET.getlist("status")
    category_filter = request.GET.getlist("category")
    priority_filter = request.GET.getlist("priority")
    table_content = request.GET.get("table-content", "tasks")
    query_param = request.GET.copy()
    
    query_param.pop('page', None)
    
    categories = Category.objects.all()
    priorities = Priority.objects.all()
    tasks = Task.objects.all()
    subtasks = SubTask.objects.all()
    notes = Note.objects.all()
    
    if status_filter:
        tasks = tasks.filter(status__in=status_filter)
        subtasks = subtasks.filter(status__in=status_filter)
        
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
        subtasks = subtasks.filter(parent_task__title__contains=search_query)
        subtasks = subtasks.filter(title__contains=search_query)
        notes = notes.filter(task__title__contains=search_query)
    
    if table_content == 'tasks':
        paginator = Paginator(tasks, 10) 
        page = request.GET.get('page')
        paginated_content = paginator.get_page(page)
    elif table_content == 'subtasks':
        paginator = Paginator(subtasks, 10) 
        page = request.GET.get('page')
        paginated_content = paginator.get_page(page)
    elif table_content == 'notes':
        paginator = Paginator(notes, 10) 
        page = request.GET.get('page')
        paginated_content = paginator.get_page(page)
        
    
    return render(request, 'home.html', {
        'content': paginated_content, 
        'categories': categories,
        'priorities': priorities,
        'query_params': query_param.urlencode(),
        'table_content': table_content})

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'create_task_view.html'
    success_url = reverse_lazy('Home_Page')