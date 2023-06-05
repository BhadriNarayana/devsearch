from django.urls import path, include
from . import views
urlpatterns = [
    path('login/', views.loginPage, name = "login"),
    path('', views.profiles, name = 'profiles'),
    path('profile/<str:pk>/', views.userProfile, name = 'profile'),

    path('logout/', views.logoutUser, name = 'logout')
]
