# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onesite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onesite_demo',
            name='onesitedemo_text',
            field=models.TextField(null=True, verbose_name=b'\xd1\x82\xd0\xb5\xd0\xba\xd1\x81\xd1\x82', blank=True),
            preserve_default=True,
        ),
    ]
