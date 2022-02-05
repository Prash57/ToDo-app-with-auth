from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.viewTasks, name='list'),
    path('add/', views.createTask, name='add'),
    path('update/<str:pk>/', views.updateTask, name='update'),
    path('delete/<str:pk>/', views.deleteTask, name='delete'),
]
