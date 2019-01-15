from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import Noteform


def social(request):
    dic = {'headerfave': '#333333', 'navn': 'Notedeling'}
    return render(request, 'bagvask/content.html', dic)


def upload(request):
    form = Noteform()
    dic = {'headerfave': '#333333', 'navn': 'upload', 'form': form}
    if request.POST == 'POST':
        form = Noteform(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.usr = request['usr']
            print('ok')
            instance.save()
    return render(request, 'bagvask/uploadpage.html', dic)
