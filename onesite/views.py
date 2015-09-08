# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from onesite.models import Onesite_Demo


# Create your views here.

def one_site_demo(request):
    name = 'one_one_site_demo'
    return render_to_response('onesite/onesitedemo_one.html', {'name', name})


def one_site_all(reques):
    # название модели.менеджер.что вывести
    to_one_site_all = Onesite_Demo.objects.all()
    return render_to_response('onesite/onesitedemo_all.html', {'to_one_site_all': to_one_site_all})
