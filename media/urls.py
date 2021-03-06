# -*- coding: utf-8 -*-
__author__ = 'integral'

from django.conf.urls import patterns, url
from media.views import index, media_all, mediaforum_all, myaudio_all, myvideo_all


urlpatterns = patterns('',
                       url(r'^$', index),
                       url(r'^all/$', media_all),
                       url(r'^mediaforumall/$', mediaforum_all),
                       url(r'^audio/$', myaudio_all),
                       url(r'^video/$', myvideo_all),

                       )
