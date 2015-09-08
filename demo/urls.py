# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from info.views import index

urlpatterns = patterns('',

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^onesite/', include('onesite.urls')),
                       url(r'^info/', include('info.urls')),
                       url(r'^media/', include('media.urls')),
                       url(r'^programming/', include('programming.urls')),
                       url(r'^$', index),
                       )
