# -*- coding: utf-8 -*-
from django.db import models


class Programmingforum(models.Model):
    """
    форум по программированию
    """

    class Meta():
        # задаем название таблицы
        db_table = 'app_programmingforum_demo'
        # Задаем как будет подписана таблица в реале
        verbose_name = 'Форум по программированию'
        # Задаем как будет подписана таблица в реале в множественном числе
        verbose_name_plural = "Форум по программированию"

    # создаем поля таблицы в базе данных
    programmingforum_tema = models.CharField(max_length=200, verbose_name='Заголовок')
    programmingforum_text = models.TextField(verbose_name='Текст', blank=True, null=True)
    programmingforum_date = models.DateTimeField(verbose_name='Дата')


    # функция возвращает название описание таблицы от поля onesitedemo_titel
    def __unicode__(self):
        return self.programmingforum_tema
