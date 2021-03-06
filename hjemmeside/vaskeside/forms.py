from django import forms
from . import models


class Reservertid(forms.ModelForm):
    class Meta:
        model = models.Tables
        fields = ['maskine', 'starttid', 'sluttid']
        labels = {'maskine': 'Maskine',
                  'starttid': 'Start tidspunkt',
                  'sluttid': 'Slut tidspunkt'}


def userwashes(user):
    thechois = [('', '----------')]
    if user.username == 'admin':
        qwery = models.Tables.objects.filter()
    else:
        qwery = models.Tables.objects.filter(usr=user)
    for i in qwery:
        temp = []
        whyslet = i.starttid + '-' + i.sluttid + '-' + i.maskine
        temp.append(whyslet)
        temp.append(whyslet)
        thechois.append(tuple(temp))
    return thechois


def choise(user):
    thechois = userwashes(user)

    class Slettid(forms.Form):
        slet_tid = forms.ChoiceField(choices=thechois)

    return Slettid()
