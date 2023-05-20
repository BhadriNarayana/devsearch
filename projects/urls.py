
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<str:pk>/', views.project, name = 'project'),
    path('', views.projects, name = 'projects'),
    path('crud/create-project/', views.create_project, name = 'create-project'),
    path('crud/upadte-project/<str:pk>/', views.update_project, name = 'update-project'),
    path('crud/delete-project/<str:pk>/', views.delete_project, name = 'delete-project'),
]




