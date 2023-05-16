from django.shortcuts import render

from django.shortcuts import HttpResponse
# Create your views here.

def sprojects(request, pk):
        
        return render(request, 'single-project.html')

def projects(request):
        return render(request, 'projects.html')
