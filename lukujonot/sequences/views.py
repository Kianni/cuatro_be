from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    return render(request, "sequences/welcome.html")

def options(request):
    return render(request, "sequences/options.html")

def displayAllSequences(request):
    return render(request, "sequences/display.html")

def addSequence(request):
    return render(request, "sequences/add.html")

def farewell(request):
    return render(request, "sequences/farewell.html")