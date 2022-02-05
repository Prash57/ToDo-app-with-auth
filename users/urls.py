from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

    path('account/', views.userAccount, name='account'),
    path('edit-account/', views.editAccount, name='edit'),
    path('delete-profile/<str:pk>/', views.deleteProfile, name='delete-profile'),
]