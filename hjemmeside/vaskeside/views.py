from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

faver = ['#9edae5',
         '#dbdb8d',
         '#c7c7c7',
         '#f7b6d2',
         '#c49c94',
         '#c5b0d5',
         '#ff9896',
         '#98df8a',
         '#ffbb78',
         '#aec7e8',
         '#9edae5',
         '#dbdb8d',
         '#c7c7c7']

favedict = {}
for index, i in zip(lsttimetable, faver):
    favedict[index] = i


def nyvask(request):
    tider = Tables.objects.all()
    navn = str(request.path)[1:][:-1].replace('-', ' ').capitalize()
    content = {'tabel': tuple(lsttimetable),
               'tider': tider,
               'navn': navn}

    return render(request, 'vask/wash.html', content)


def frontpage(request):
    return redirect('Sønderhus vask 1')


@login_required(login_url='logind')
def reservertid(request):
    form = forms.Reservertid()
    dic = {'form': form, 'navn': 'Reserver tid', 'headerfave': '#f6f6f6'}

    if request.method == 'POST':
        form = forms.Reservertid(request.POST)
        currentmaskine = request.POST['maskine']
        templist = []
        for m in maskiner:
            templist.append(m[0])
        if request.POST['maskine'] in templist:
            pass
        else:
            # Hvis de prøver på noget
            dic['virkede'] = 'hvad prøver du på {}'.format(str(request.user))
            return render(request, 'vask/form.html', dic)
        valid = notavtime([request.POST['starttid'], request.POST['sluttid']], request.POST['maskine'])

        if valid[0]:
            # Hvis det virede
            fave = favedict[request.POST['starttid']]
            instance = form.save(commit=False)
            instance.usr = request.user
            instance.columnlen = valid[1]
            instance.color = fave
            instance.save()

            return redirect(currentmaskine)
        else:
            # Hvis det ikke virkede
            dic['virkede'] = 'Jeg tror tiden nok er tagt eller noget'
            return render(request, 'vask/form.html', dic)

    return render(request, 'vask/form.html', dic)


@login_required(login_url='logind')
def slettid(request):
    form = forms.choise(request.user)
    dic = {'form': form, 'virkede': '', 'navn': 'Slet tid', 'headerfave': '#f6f6f6'}
    formitems = forms.userwashes(request.user)
    if request.method == 'POST':
        che = []
        for i in formitems:
            che.append(i[0].replace('-', ' '))
        if request.POST['slet_tid'].replace('-', ' ') in che:
            pass
        else:
            return render(request, 'vask/form.html',
                          {'form': form, 'virkede': 'fuck dig du '
                                                    'troede person der bor på {}'.format(request.user),
                                                    'navn': 'Slet tid'})
        view = request.POST['slet_tid'].split('-')
        starttid, sluttid, maskine = view
        Tables.objects.filter(starttid=starttid, sluttid=sluttid, maskine=maskine).delete()
        m = maskine
        return redirect(m)
    return render(request, 'vask/form.html', dic)


def logind_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Reserver tid')
    else:
        form = AuthenticationForm()
        form.error_messages['invalid_login'] = 'prøv igen... måske skrev du forkert'
    return render(request, 'vask/logind.html', {'form': form, 'navn': 'Logind'})


def coolshit(request):
    return render(request, 'vask/coolshit.html')
