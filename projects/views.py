from django.shortcuts import render

from django.shortcuts import HttpResponse
# Create your views here.

def projetcs(request):
    return HttpResponse("Projects Main page")


def hpage(request):
    return HttpResponse("Home Page")