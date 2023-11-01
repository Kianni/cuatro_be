from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    return HttpResponse("start")

def options(request):
    return HttpResponse("display all or add a new")

def displayAllSequences(request):
    return HttpResponse("display all")

def addSequence(request):
    return HttpResponse("add a new")

def farewell(request):
    return HttpResponse("stop")