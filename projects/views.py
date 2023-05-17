from django.shortcuts import render
from .models import Project, Review, Tag
from django.shortcuts import HttpResponse
# Create your views here.

def project(request, pk):
        project = Project.objects.get(id = pk)        
        return render(request, 'projects/single-project.html', {'project':project})

def projects(request):
        projects = Project.objects.all()
        return render(request, 'projects/projects.html', {'projects':projects})

