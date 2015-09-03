#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Onesite_Demo(models.Model):

    """
    Сайт описание того то
    """
    class Meta():
        # задаем название таблицы
        db_table = 'app_onesite_demo'
        # Задаем как будет подписана таблица в реале
        verbose_name='Одиночный сайт'
    # создаем поля таблицы в базе данных
    onesitedemo_titel = models.CharField(max_length=200,verbose_name='Заголовок')
    onesitedemo_text = models.TextField(verbose_name='Текст', blank=True, null=True)
    onesitedemo_date = models.DateTimeField(verbose_name='Дата')
    onesitedemo_text1 = models.TextField(verbose_name='Текст1', blank=True, null=True)

    def __unicode__(self):
        return self.onesitedemo_titel

# приететттпппппп