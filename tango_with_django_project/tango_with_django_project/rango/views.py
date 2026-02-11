from django.shortcuts import render
# this part is allowing to add indexes to a project
from django.http import HttpResponse


def index(request):
    return HttpResponse("Test")

def about(request):
    return HttpResponse("Rango says here is the about page.")