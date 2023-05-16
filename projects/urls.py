
from django.urls import path
from . import views
urlpatterns = [
    path('', views.hpage),
    path('pj/<str:pk>/', views.projetcs),
]
