# -*- coding: utf-8 -*-
__author__ = 'integral'

from django.conf.urls import patterns, url
from programming.views import programmingforum

urlpatterns = patterns('',
                       url(r'^forum/$', programmingforum),

                       )