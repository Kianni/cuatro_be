from django import forms

class SequenceSearchForm(forms.Form):
    name = forms.CharField(label='Search by Name', max_length=100)