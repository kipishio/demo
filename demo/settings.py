#-*- coding: utf-8 -*-
"""
Django settings for demo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
# указываем путь который везде будем езать это основная аппка в которой лежит проект D:\General\DjangoProject\demo
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# секретный ключ для работы сайта
SECRET_KEY = 'yyz5p2&m5a4nxjnkgk&kwv!hf-kph%=b2!@e(p&i222d03^s9-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'onesite',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'demo.urls'

WSGI_APPLICATION = 'demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
# указываем название базы данных и параметры подключения и прочее
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'demo_db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
# название  папак которые будут сздаваться для статических файлов, в папках с таким именем джанго будет искать
# статические файлы
STATIC_URL = '/static/'

# указываем папку куда будут собираться статические файлы проекта
# должен получиться адрес такой 'D:/General/DjangoProject/demo/static'
STATIC_ROOT = (os.path.join(BASE_DIR, 'static'))

print('_______________')
print(STATIC_ROOT)
#  пути к папкам с шаблонами, на сервере если не указать будет ошибка
# примерно такие пути должны быть 'D:/General/DjangoProject/demo\\templates' и
# 'D:/General/DjangoProject/demo\\onesite/templates'
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
    os.path.join(BASE_DIR, 'onesite/templates'),
)
print(TEMPLATE_DIRS)

#  порядок поиска шаблонов
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
)

print(TEMPLATE_LOADERS)

# находит статические файлы данная функция
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)