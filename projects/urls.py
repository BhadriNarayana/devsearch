
from django.urls import path
from . import views
urlpatterns = [
    path('<str:pk>/', views.project, name = 'projects'),
    path('', views.projects, name = 'project')
]
