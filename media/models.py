# -*- coding: utf-8 -*-
from django.db import models


class MediaDemo(models.Model):
    """
    Все про медиа
    """

    class Meta:
        # задаем название таблицы
        db_table = 'app_media_demo'
        # Задаем как будет подписана таблица в реале
        verbose_name = 'Все о медиа'
        # Задаем как будет подписана таблица в реале в множественном числе
        verbose_name_plural = "Все о медиа"

    # создаем поля таблицы в базе данных
    mediademo_tema = models.CharField(max_length=200, verbose_name='Заголовок')
    mediademo_text = models.TextField(verbose_name='Текст', blank=True, null=True)
    mediademo_date = models.DateTimeField(verbose_name='Дата')

    # функция возвращает название описание таблицы от поля mediademo_opisanie
    def __unicode__(self):
        return self.mediademo_tema


class MediaForumDemo(models.Model):
    """
        Медиа форум, обсуждаем знакомимся
    """

    class Meta:
        # задаем название таблицы
        db_table = 'app_mediaforum_demo'
        # Задаем как будет подписана таблица в реале
        verbose_name = 'Медиа форум'
        # Задаем как будет подписана таблица в реале в множественном числе
        verbose_name_plural = "Медиа форум"

    # создаем поля таблицы в базе данных
    mediaforumdemo_tema = models.CharField(max_length=200, verbose_name='Заголовок')
    mediaforumdemo_text = models.TextField(verbose_name='Текст', blank=True, null=True)
    mediaforumdemo_date = models.DateTimeField(verbose_name='Дата')

    # функция возвращает название описание таблицы от поля mediademo_opisanie
    def __unicode__(self):
        return self.mediaforumdemo_tema


class MyAudio(models.Model):
    """
        Моя музыка
    """

    class Meta:
        # задаем название таблицы
        db_table = 'app_myaudio_demo'
        # Задаем как будет подписана таблица в реале
        verbose_name = 'Моя музыка'
        # Задаем как будет подписана таблица в реале в множественном числе
        verbose_name_plural = "Моя музыка"

    # создаем поля таблицы в базе данных
    myaudiodemo_tema = models.CharField(max_length=200, verbose_name='Заголовок')
    myaudiodemo_text = models.TextField(verbose_name='Текст', blank=True, null=True)
    myaudiodemo_date = models.DateTimeField(verbose_name='Дата')

    # функция возвращает название описание таблицы от поля myaudiodemo_tema
    def __unicode__(self):
        return self.myaudiodemo_tema

class MyVideo(models.Model):
    """
        Моё видео
    """

    class Meta:
        # задаем название таблицы
        db_table = 'app_myvideodemo_demo'
        # Задаем как будет подписана таблица в реале
        verbose_name = 'Моё видео'
        # Задаем как будет подписана таблица в реале в множественном числе
        verbose_name_plural = "Моё видео"

    # создаем поля таблицы в базе данных
    myvideodemo_tema = models.CharField(max_length=200, verbose_name='Заголовок')
    myvideodemo_text = models.TextField(verbose_name='Текст', blank=True, null=True)
    myvideodemo_date = models.DateTimeField(verbose_name='Дата')

    # функция возвращает название описание таблицы от поля myvideodemo_tema
    def __unicode__(self):
        return self.myvideodemo_tema
