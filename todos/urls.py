from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home_Page'),
    path('task/create/', views.TaskCreateView.as_view(), name='create_task'),
    path('task/<int:pk>/edit/', views.TaskUpdateView.as_view(), name='update_task'),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='delete_task'),
    path('subtask/create/', views.SubtaskCreateView.as_view(), name='create_subtask'),
    path('subtask/<int:pk>/edit/', views.SubtaskUpdateView.as_view(), name='update_subtask'),
    path('subtask/<int:pk>/delete/', views.SubtaskDeleteView.as_view(), name='delete_subtask'),
    path('note/create/', views.NoteCreateView.as_view(), name='create_note'),
    path('note/<int:pk>/edit/', views.NoteUpdateView.as_view(), name='update_note'),
    path('note/<int:pk>/delete/', views.NoteDeleteView.as_view(), name='delete_note')
]
