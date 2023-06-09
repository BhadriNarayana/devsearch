from django.shortcuts import render
from .models import Project, Review, Tag
from django.shortcuts import HttpResponse, redirect
from django.contrib.auth.decorators import login_required 
from .forms import ProjectForm, ReviewForm
from .utils import searchProjects, paginateProjects

from django.contrib import messages

# Create your views here.

def project(request, pk):
        project = Project.objects.get(id = pk)
        form = ReviewForm() 

        if request.method == 'POST':
                form = ReviewForm(request.POST)
                review = form.save(commit = False)
                review.owner = request.user.profile
                review.project = project
                review.save()      

                project.getVoteCount
                messages.success(request, "Successfully posted your review")
                return redirect('project', pk = project.id)  

               
        return render(request, 'projects/single-project.html', {'project':project, 'form':form})

def projects(request):       
        projects, search_query = searchProjects(request)

        custom_range, projects =  paginateProjects(request, projects, 3)
  

        context = {'projects':projects, 'search_query':search_query, 'custom_range': custom_range}                        


        return render(request, 'projects/projects.html', context)

@login_required(login_url = "login")
def create_project(request):
        profile = request.user.profile
        form = ProjectForm()

        if request.method == 'POST':
                form = ProjectForm(request.POST, request.FILES)

                if form.is_valid():
                        project = form.save(commit = False)
                        project.owner = profile
                        project.save()
                        return redirect('account')

        

        return render(request, 'projects/project-form.html', {'form':form, 'tp':3})


@login_required(login_url = "login")
def update_project(request, pk):
        profile = request.user.profile
        project = profile.project_set.get(id = pk)

        form = ProjectForm(instance = project)

        if request.method == 'POST':
                form = ProjectForm(request.POST,request.FILES, instance = project)

                if form.is_valid():
                        form.save()
                        return redirect('account')


        return render(request, 'projects/project-form.html', {'form':form})

@login_required(login_url = "login")
def delete_project(request, pk):
        
        profile = request.user.profile
        project = profile.project_set.get(id = pk)

        if request.method == 'POST':
                project.delete()
                return redirect('account')

        return render(request, 'delete-object.html', {'object':project})