from django.shortcuts import render

from django.shortcuts import HttpResponse
# Create your views here.

def project(request, pk):        
        return render(request, 'projects/single-project.html')

def projects(request):
        return render(request, 'projects/projects.html')
