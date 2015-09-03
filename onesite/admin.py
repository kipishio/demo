#-*- coding: utf-8 -*-
from django.contrib import admin
# импортируем модели из файлв model.py
from onesite.models import Onesite_Demo

# регистрируем модели из файлв model.py
admin.site.register(Onesite_Demo)
# Register your models here.
