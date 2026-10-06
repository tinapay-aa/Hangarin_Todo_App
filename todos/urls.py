from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home_Page'),
    path('task/create/', views.TaskCreateView.as_view(), name='Create_Task'),
    path('task/<int:pk>/edit/', views.TaskUpdateView.as_view(), name='Update_Task'),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='Delete_Task')
]
