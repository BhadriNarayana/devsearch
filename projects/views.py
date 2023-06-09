from django.shortcuts import render
from .models import Project, Review, Tag
from django.shortcuts import HttpResponse, redirect
from django.contrib.auth.decorators import login_required 
from .forms import ProjectForm
from .utils import searchProjects


from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

def project(request, pk):
        project = Project.objects.get(id = pk)        
        return render(request, 'projects/single-project.html', {'project':project})

def projects(request):       
        projects, search_query = searchProjects(request)

        page = request.GET.get('page')
        results = 3

        paginator = Paginator(projects, results)

        try:
                projects = paginator.page(page)
        except PageNotAnInteger:
                page = 1
                projects = paginator.page(page)

        except EmptyPage:
                page = paginator.num_pages
                projects = paginator.page(page)                


        return render(request, 'projects/projects.html', {'projects':projects, 'search_query':search_query})

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