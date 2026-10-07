from django.shortcuts import render
from django.http import HttpResponse   
from .models import Task, Category, Priority, SubTask, Note
from .forms import TaskForm, SubtaskForm, NotesForm
from django.core.paginator import Paginator
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

@login_required
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
        
    return render(request, 'todos/home.html', {
        'content': paginated_content, 
        'categories': categories,
        'priorities': priorities,
        'query_params': query_param.urlencode(),
        'table_content': table_content})

class TaskCreateView(CreateView, LoginRequiredMixin):
    model = Task
    form_class = TaskForm
    template_name = 'todos/Task/create_task.html'
    success_url = reverse_lazy('Home_Page')
    
    def get_success_url(self):
        query_params = self.request.GET.urlencode()
        
        if query_params:
            return f'/?{query_params}'
        else:
            return '/'

class TaskUpdateView(UpdateView, LoginRequiredMixin):
    model = Task
    form_class = TaskForm
    template_name = 'todos/Task/update_task.html'
    success_url = reverse_lazy('Home_Page')
    
    def get_success_url(self):
        query_params = self.request.GET.urlencode()
        
        if query_params:
            return f'/?{query_params}'
        else:
            return '/'
    
class TaskDeleteView(DeleteView, LoginRequiredMixin):
    model = Task
    template_name = 'todos/Task/delete_task.html'
    success_url = reverse_lazy('Home_Page')
    
    def get_success_url(self):
        query_params = self.request.GET.urlencode()
        
        if query_params:
            return f'/?{query_params}'
        else:
            return '/'
    
class SubtaskCreateView(CreateView, LoginRequiredMixin):
    model = SubTask
    form_class = SubtaskForm
    template_name = 'todos/Subtask/create_subtask.html'
    success_url = reverse_lazy('Home_Page')
    
    def get_success_url(self):
        query_params = self.request.GET.urlencode()
        
        if query_params:
            return f'/?{query_params}'
        else:
            return '/'

class SubtaskUpdateView(UpdateView, LoginRequiredMixin):
    model = SubTask
    form_class = SubtaskForm
    template_name = 'todos/Subtask/update_subtask.html'
    success_url = reverse_lazy('Home_Page')
    
    def get_success_url(self):
        query_params = self.request.GET.urlencode()
        
        if query_params:
            return f'/?{query_params}'
        else:
            return '/'

class SubtaskDeleteView(DeleteView, LoginRequiredMixin):
    model = SubTask
    template_name = 'todos/Subtask/delete_subtask.html'
    success_url = reverse_lazy('Home_Page')
    
    def get_success_url(self):
        query_params = self.request.GET.urlencode()
        
        if query_params:
            return f'/?{query_params}'
        else:
            return '/'
    
class NoteCreateView(CreateView, LoginRequiredMixin):
    model = Note
    form_class = NotesForm
    template_name = 'todos/Note/create_note.html'
    success_url = reverse_lazy('Home_Page')
    
    def get_success_url(self):
        query_params = self.request.GET.urlencode()
        
        if query_params:
            return f'/?{query_params}'
        else:
            return '/'

class NoteUpdateView(UpdateView, LoginRequiredMixin):
    model = Note
    form_class = NotesForm
    template_name = 'todos/Note/update_note.html'
    success_url = reverse_lazy('Home_Page')
    
    def get_success_url(self):
        query_params = self.request.GET.urlencode()
        
        if query_params:
            return f'/?{query_params}'
        else:
            return '/'

class NoteDeleteView(DeleteView, LoginRequiredMixin):
    model = Note
    template_name = 'todos/Note/delete_note.html'
    success_url = reverse_lazy('Home_Page')
    
    def get_success_url(self):
        query_params = self.request.GET.urlencode()
        
        if query_params:
            return f'/?{query_params}'
        else:
            return '/'