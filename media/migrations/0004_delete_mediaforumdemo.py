# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0003_auto_20150908_1601'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MediaForumDemo',
        ),
    ]
