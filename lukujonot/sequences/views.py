from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    return render(request, "sequences/welcome.html")

def options(request):
    return render(request, "sequences/options.html")

def displayAllSequences(request):
    return render(request, "sequences/display.html")

def addSequence(request):
    return HttpResponse("add a new")

def farewell(request):
    return HttpResponse("stop")