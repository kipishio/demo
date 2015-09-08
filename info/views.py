# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response


# Create your views here.

def index(request):
    index = 'index'
    return render_to_response('info/index.html', {'index', index})


def avtobiographi(request):
    avtobiograph = 'Автобиография'
    return render_to_response('info/avtobiographi.html', {'avtobiographi': avtobiograph})


def kontakti(request):
    kontakt = 'список контактов'
    return render_to_response('info/kontakti.html', {'kontakti': kontakt})


def oproekte(request):
    oproekt = 'Проект такой то сделан тогда то'
    return render_to_response('info/oproekte.html', {'oproekte': oproekt})


def druzya(request):
    druzy = 'Список друзей проекта'
    return render_to_response('info/druzya.html', {'druzya': druzy})
