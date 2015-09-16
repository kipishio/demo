# -*- coding: utf-8 -*-
__author__ = 'Юля'

from django.conf.urls import patterns, url
from myforms.views import MyNameForm, mynametest

from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', mynametest),
                       )
