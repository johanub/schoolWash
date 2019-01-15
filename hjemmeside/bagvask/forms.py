from django import forms
from . import models


class Noteform(forms.ModelForm):
    class Meta:
        model = models.Noter
        fields = ['note', 'titel', 'beskrivelse']
        labels = {'note': 'Note som PDF(skal være PDF)',
                  'titel': 'Titel:',
                  'beskrivelse': 'Beskrivelse:'}

