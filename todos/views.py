from django.shortcuts import render
from django.http import HttpResponse   
from .models import Task, Category, Priority, SubTask, Note
from .forms import TaskForm, SubtaskForm, NotesForm
from django.core.paginator import Paginator
from django.views.generic import CreateView, UpdateView, DeleteView
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
    
    if search_query:
        tasks = tasks.filter(title__contains=search_query)
        subtasks = subtasks.filter(parent_task__title__contains=search_query)
        subtasks = subtasks.filter(title__contains=search_query)
        notes = notes.filter(task__title__contains=search_query)
    
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
    template_name = 'Task/create_task.html'
    success_url = reverse_lazy('Home_Page')
    
    def get_success_url(self):
        query_params = self.request.GET.urlencode()
        
        if query_params:
            return f'/?{query_params}'
        else:
            return '/'

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'Task/update_task.html'
    success_url = reverse_lazy('Home_Page')
    
    def get_success_url(self):
        query_params = self.request.GET.urlencode()
        
        if query_params:
            return f'/?{query_params}'
        else:
            return '/'
    
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'Task/delete_task.html'
    success_url = reverse_lazy('Home_Page')
    
    def get_success_url(self):
        query_params = self.request.GET.urlencode()
        
        if query_params:
            return f'/?{query_params}'
        else:
            return '/'
    
class SubtaskCreateView(CreateView):
    model = SubTask
    form_class = SubtaskForm
    template_name = 'Subtask/create_subtask.html'
    success_url = reverse_lazy('Home_Page')
    
    def get_success_url(self):
        query_params = self.request.GET.urlencode()
        
        if query_params:
            return f'/?{query_params}'
        else:
            return '/'

class SubtaskUpdateView(UpdateView):
    model = SubTask
    form_class = SubtaskForm
    template_name = 'Subtask/update_subtask.html'
    success_url = reverse_lazy('Home_Page')
    
    def get_success_url(self):
        query_params = self.request.GET.urlencode()
        
        if query_params:
            return f'/?{query_params}'
        else:
            return '/'

class SubtaskDeleteView(DeleteView):
    model = SubTask
    template_name = 'Subtask/delete_subtask.html'
    success_url = reverse_lazy('Home_Page')
    
    def get_success_url(self):
        query_params = self.request.GET.urlencode()
        
        if query_params:
            return f'/?{query_params}'
        else:
            return '/'
    
class NoteCreateView(CreateView):
    model = Note
    form_class = NotesForm
    template_name = 'Note/create_note.html'
    success_url = reverse_lazy('Home_Page')
    
    def get_success_url(self):
        query_params = self.request.GET.urlencode()
        
        if query_params:
            return f'/?{query_params}'
        else:
            return '/'

class NoteUpdateView(UpdateView):
    model = Note
    form_class = NotesForm
    template_name = 'Note/update_note.html'
    success_url = reverse_lazy('Home_Page')
    
    def get_success_url(self):
        query_params = self.request.GET.urlencode()
        
        if query_params:
            return f'/?{query_params}'
        else:
            return '/'

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'Note/delete_note.html'
    success_url = reverse_lazy('Home_Page')
    
    def get_success_url(self):
        query_params = self.request.GET.urlencode()
        
        if query_params:
            return f'/?{query_params}'
        else:
            return '/'