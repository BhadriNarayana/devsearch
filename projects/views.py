from django.shortcuts import render

from django.shortcuts import HttpResponse
# Create your views here.

def projetcs(request, pk):
    return HttpResponse(f"Project number {pk}")


def hpage(request):
    return HttpResponse("Home Page of projects")