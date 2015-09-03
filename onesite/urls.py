#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from onesite.views import one_site_all
__author__ = 'Юля'

urlpatterns = patterns('',
    # Examples:
    # onesite

    url(r'^all/$', one_site_all ),

)
