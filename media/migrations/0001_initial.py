# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mediademo_opisanie', models.CharField(max_length=200, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xba')),
                ('mediademo_text', models.TextField(null=True, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82', blank=True)),
                ('mediademo_date', models.DateTimeField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0')),
            ],
            options={
                'db_table': 'app_media_demo',
                'verbose_name': '\u0412\u0441\u0435 \u043e \u043c\u0435\u0434\u0438\u0430',
                'verbose_name_plural': '\u0412\u0441\u0435 \u043e \u043c\u0435\u0434\u0438\u0430',
            },
            bases=(models.Model,),
        ),
    ]
