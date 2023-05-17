from django.shortcuts import render
from .models import Project, Review, Tag
from django.shortcuts import HttpResponse

from .forms import ProjectForm
# Create your views here.

def project(request, pk):
        project = Project.objects.get(id = pk)        
        return render(request, 'projects/single-project.html', {'project':project})

def projects(request):
        projects = Project.objects.all()
        return render(request, 'projects/projects.html', {'projects':projects})

def create_project(request):

        form = ProjectForm()

        return render(request, 'projects/project-form.html', {'form':form})