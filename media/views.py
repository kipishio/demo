# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from  media.models import MediaForumDemo, MediaDemo, MyAudio, MyVideo


def index(request):
    medi = 'Все по медиоинфе'
    return render_to_response('media/index.html', {'medi': medi})


def media_all(reques):
    # название модели.менеджер.что вывести
    to_media_all = MediaDemo.objects.all()
    return render_to_response('media/media_all.html', {'to_media_all': to_media_all})


def mediaforum_all(reques):
    # название модели.менеджер.что вывести
    to_mediaforum_all = MediaForumDemo.objects.all()
    return render_to_response('media/mediaforum.html', {'to_mediaforum_all': to_mediaforum_all})


def myaudio_all(reques):
    # название модели.менеджер.что вывести
    to_myaudio_all = MyAudio.objects.all()
    return render_to_response('media/myaudio.html', {'to_myaudio_all': to_myaudio_all})


def myvideo_all(reques):
    # название модели.менеджер.что вывести
    to_myvideo_all = MyVideo.objects.all()
    return render_to_response('media/myvideo.html', {'to_myvideo_all': to_myvideo_all})
