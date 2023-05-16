from django.shortcuts import render

from django.shortcuts import HttpResponse
# Create your views here.

def sprojects(request):
        
        return render(request, 'single-project.html')

def projects(request, pk):
        if pk == None:
                return render(request, 'projects.html')
        return render(request, 'single-project.html')
