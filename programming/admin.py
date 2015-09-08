# -*- coding: utf-8 -*-
from django.contrib import admin

# импортируем модели из файлв model.py
from programming.models import Programmingforum

# регистрируем модели из файлв model.py
admin.site.register(Programmingforum)

# Register your models here.
