from django.urls import path, include
from . import views
urlpatterns = [
    path('login/', views.loginUser, name = "login"),
    path('logout/', views.logoutUser, name = 'logout'),
    path('register/', views.registerUser, name = 'register'),
    path('', views.profiles, name = 'profiles'),
    path('profile/<str:pk>/', views.userProfile, name = 'profile'),

    path('edit-account/', views.editAccount, name = 'edit-account'),
    path('account/', views.userAccount, name = 'account'),   
    path('create-skill', views.createSkill, name = "create-skill"),
]
