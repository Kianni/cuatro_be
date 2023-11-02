from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from sequences.forms import SequenceSearchForm
from sequences.models import Sequence

def welcome(request):
    return render(request, "sequences/welcome.html")

def options(request):
    return render(request, "sequences/options.html")

def displayAllSequences(request):
    # Default sorting is none
    sort_option = request.GET.get('sort', 'none')

    if sort_option == 'asc':
        sequences = Sequence.objects.all().order_by('name')  # Sort sequences by name in ascending order
    else:
        sequences = Sequence.objects.all()  # No sorting

    search_form = SequenceSearchForm()

    if request.method == 'POST':
        search_form = SequenceSearchForm(request.POST)
        if search_form.is_valid():
            name = search_form.cleaned_data['name']
            sequences = sequences.filter(name__icontains=name)

    # Check for the "Show All" parameter
    show_all = request.GET.get('show_all')
    if show_all:
        if sort_option == 'asc':
            sequences = Sequence.objects.all().order_by('name')  # Reset the filter with sorting
        else:
            sequences = Sequence.objects.all()  # Reset the filter without sorting

    return render(request, "sequences/display.html", {"sequences": sequences, "search_form": search_form})

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