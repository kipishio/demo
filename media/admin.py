# -*- coding: utf-8 -*-
from django.contrib import admin

# импортируем модели из файлв model.py
from media.models import MediaDemo, MediaForumDemo, MyVideo, MyAudio

# регистрируем модели из файлв model.py
admin.site.register(MediaDemo)
admin.site.register(MediaForumDemo)
admin.site.register(MyAudio)
admin.site.register(MyVideo)

