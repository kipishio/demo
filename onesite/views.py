#-*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from onesite.models import Onesite_Demo

# Create your views here.

def one_site_demo(request):
    name = 'one_one_site_demo'
    return render_to_response('onesitedemo_one.html',{'name',name})


def one_site_all(reques):
    # название модели.менеджер.что вывести
    to = Onesite_Demo.objects.all()
    print('111111111')

    return render_to_response('onesitedemo_all.html',{'to':to})