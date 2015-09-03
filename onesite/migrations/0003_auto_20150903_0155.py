# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onesite', '0002_auto_20150903_0140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='onesite_demo',
            options={'verbose_name': '\u041e\u0434\u0438\u043d\u043e\u0447\u043d\u044b\u0439 \u0441\u0430\u0439\u0442'},
        ),
        migrations.AddField(
            model_name='onesite_demo',
            name='onesitedemo_text1',
            field=models.TextField(null=True, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='onesite_demo',
            name='onesitedemo_date',
            field=models.DateTimeField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='onesite_demo',
            name='onesitedemo_text',
            field=models.TextField(null=True, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='onesite_demo',
            name='onesitedemo_titel',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xba'),
            preserve_default=True,
        ),
    ]
