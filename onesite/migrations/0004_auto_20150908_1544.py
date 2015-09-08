# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onesite', '0003_auto_20150903_0155'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='onesite_demo',
            options={'verbose_name': '\u041e\u0434\u0438\u043d\u043e\u0447\u043d\u044b\u0439 \u0441\u0430\u0439\u0442', 'verbose_name_plural': '\u041e\u0434\u0438\u043d\u043e\u0447\u043d\u044b\u0435 \u0441\u0430\u0439\u0442\u044b'},
        ),
        migrations.AlterField(
            model_name='onesite_demo',
            name='onesitedemo_text1',
            field=models.TextField(null=True, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x821', blank=True),
            preserve_default=True,
        ),
    ]
