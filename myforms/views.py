# -*- coding: utf-8 -*-
# Create your views here.

from myforms.forms import MyNameForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render


def myname(reqvest):
    if reqvest.method == 'POST':
        form = MyNameForm(reqvest.POST)
        if form.is_valid():
            return HttpResponseRedirect('ссылка')

    else:
        form = MyNameForm()
    return render('forms.html', {'form': 'dddddddddddd'})


def mynametest(reqvest):
    return render_to_response('forms/forms.html', {'form': 'dddddddddddd'})
