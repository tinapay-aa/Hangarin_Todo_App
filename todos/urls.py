from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home_Page'),
    path('task/create/', views.TaskCreateView.as_view(), name='Create_Task')
]
