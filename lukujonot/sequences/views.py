from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    return render(request, "sequences/welcome.html")

def options(request):
    return render(request, "sequences/options.html")

def displayAllSequences(request):
    return render(request, "sequences/display.html",
                  {"sequences": [
                      {"eka": [1,2,3,4]},
                      {"toka": [1, 3, 5]},
                      {"vika": [2, 4, 6]},
                  ]
                  })

def addSequence(request):
    return render(request, "sequences/add.html")

def farewell(request):
    return render(request, "sequences/farewell.html")