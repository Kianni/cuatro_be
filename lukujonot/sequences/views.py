from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    return HttpResponse("a1 + 3(n-1)")
