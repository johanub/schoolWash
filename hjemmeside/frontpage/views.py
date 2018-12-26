from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

tidsfaver = {}
for maskine in maskiner:
    tidsfaver.update({maskine[0]: []})


def nyvask(request):
    tider = Tables.objects.all()
    navn = str(request.path)[1:][:-1].replace('-', ' ').capitalize()
    content = {'tabel': tuple(lsttimetable),
               'tider': tider,
               'navn': navn}

    return render(request, 'washsite/wash.html', content)


def frontpage(request):
    return render(request, 'washsite/frontpage.html')


@login_required(login_url='logind')
def reservertid(request):
    form = forms.Reservertid()
    dic = {'form': form, 'navn': 'Reserver tid'}

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
            return render(request, 'washsite/form.html', dic)
        valid = notavtime([request.POST['starttid'], request.POST['sluttid']], request.POST['maskine'])

        if valid[0]:
            # Hvis det virede
            fave = tidsfaver[str(currentmaskine)]
            instance = form.save(commit=False)
            instance.usr = request.user
            instance.columnlen = valid[1]
            if not fave:
                fave.extend(('#fff6a1',
                             '#fbbaaa',
                             '#eec8f9',
                             '#a1e0f2',
                             '#bbecb6'))

            instance.color = fave.pop()
            instance.save()

            return redirect(currentmaskine)
        else:
            # Hvis det ikke virkede
            dic['virkede'] = 'Jeg tror tiden nok er tagt eller noget'
            return render(request, 'washsite/form.html', dic)

    return render(request, 'washsite/form.html', dic)


@login_required(login_url='logind')
def slettid(request):
    form = forms.choise(request.user)
    formitems = forms.userwashes(request.user)
    if request.method == 'POST':
        che = []
        for i in formitems:
            che.append(i[0].replace('-', ' '))
        if request.POST['slet_tid'].replace('-', ' ') in che:
            pass
        else:
            return render(request, 'washsite/form.html',
                          {'form': form, 'virkede': 'fuck dig du '
                                                    'troede person der bor på {}'.format(request.user),
                                                    'navn': 'Slet tid'})
        view = request.POST['slet_tid'].split('-')
        starttid, sluttid, maskine = view
        tider = [starttid, sluttid]
        rmtimes = converttimespace(converttime(tider))
        for i in rmtimes:
            Taken.objects.filter(time=i, maskine=maskine).delete()
        Tables.objects.filter(starttid=starttid, sluttid=sluttid, maskine=maskine).delete()
        m = maskine
        b = "".join([c for c in m if c != " "])
        return redirect(b.lower())
    return render(request, 'washsite/form.html', {'form': form, 'virkede': '', 'navn': 'Slet tid'})


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
    return render(request, 'accounts/logind.html', {'form': form, 'navn': 'Logind'})

