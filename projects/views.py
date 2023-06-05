from django.shortcuts import render
from .models import Project, Review, Tag
from django.shortcuts import HttpResponse, redirect
from django.contrib.auth.decorators import login_required 
from .forms import ProjectForm
# Create your views here.

def project(request, pk):
        project = Project.objects.get(id = pk)        
        return render(request, 'projects/single-project.html', {'project':project})

def projects(request):
        projects = Project.objects.all()
        return render(request, 'projects/projects.html', {'projects':projects})

def create_project(request):

        if request.method == 'POST':
                form = ProjectForm(request.POST, request.FILES)

                if form.is_valid():
                        form.save()
                        return redirect('projects')

        form = ProjectForm()

        return render(request, 'projects/project-form.html', {'form':form, 'tp':3})



def update_project(request, pk):
        project = Project.objects.get(id = pk)

        form = ProjectForm(instance = project)

        if request.method == 'POST':
                form = ProjectForm(request.POST,request.FILES, instance = project)

                if form.is_valid():
                        form.save()
                        return redirect('projects')


        return render(request, 'projects/project-form.html', {'form':form})


def delete_project(request, pk):
        project = Project.objects.get(id = pk)

        if request.method == 'POST':
                project.delete()
                return redirect('projects')

        return render(request, 'projects/delete-object.html', {'project':project})