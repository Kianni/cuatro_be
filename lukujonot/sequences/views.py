from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render
from sequences.models import Sequence

def welcome(request):
    return render(request, "sequences/welcome.html")

def options(request):
    return render(request, "sequences/options.html")

def displayAllSequences(request):
    sequences = Sequence.objects.all()

    # Iterate through the sequences and calculate the first seven terms for each
    for sequence in sequences:
        sequence.first_seven_terms = sequence.generate_first_seven_terms()

    return render(request, "sequences/display.html", {"sequences": sequences})

SequenceForm = modelform_factory(Sequence, exclude=[])

def addSequence(request):
    form = SequenceForm()
    return render(request, "sequences/add.html", {"form": form})

def farewell(request):
    return render(request, "sequences/farewell.html")