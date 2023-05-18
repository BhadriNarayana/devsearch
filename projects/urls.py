
from django.urls import path
from . import views
urlpatterns = [
    path('<str:pk>/', views.project, name = 'project'),
    path('', views.projects, name = 'projects'),
    path('create-project/', views.create_project, name = 'create-project'),
    path('upadte-project/<str:pk>/', views.update_project, name = 'update-project'),
]
