
from django.urls import path
from . import views
urlpatterns = [
    path('<str:pk>/', views.sprojects),
    path('', views.projects)
]
