from django.shortcuts import render
# this part is allowing to add indexes to a project
from django.http import HttpResponse


def index(request):
    return HttpResponse("How to build ur masles")
