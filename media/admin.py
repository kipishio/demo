# -*- coding: utf-8 -*-
from django.contrib import admin

# импортируем модели из файлв model.py
from media.models import MediaDemo, MediaForumDemo

# регистрируем модели из файлв model.py
admin.site.register(MediaDemo)
admin.site.register(MediaForumDemo)

