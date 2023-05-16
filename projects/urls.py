
from django.urls import path
from . import views
urlpatterns = [
    path('', views.hpage),
    path('projects/', views.projetcs),
]
