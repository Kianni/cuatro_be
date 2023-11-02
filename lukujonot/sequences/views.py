from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
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
    if request.method == "POST":
        form = SequenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("display")
    else:
        form = SequenceForm()
    return render(request, "sequences/add.html", {"form": form})

def farewell(request):
    return render(request, "sequences/farewell.html")

def delete_sequence(request, sequence_id):
    sequence = get_object_or_404(Sequence, id=sequence_id)
    if request.method == 'POST':
        sequence.delete()
        return redirect('display')  # Redirect to the sequence display page
    return render(request, 'sequences/display', {'sequence': sequence})