from django.http import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def alfis(request):
    return HttpResponse("Hello, Alfis!")

def jeff(request):
    return HttpResponse("Hello, Jeff!")

def greet(request, name):
    return render(request, "hello/greet.html", {"name": name.capitalize()})