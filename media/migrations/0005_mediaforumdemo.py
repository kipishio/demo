# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0004_delete_mediaforumdemo'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaForumDemo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mediaforumdemo_tema', models.CharField(max_length=200, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xba')),
                ('mediaforumdemo_text', models.TextField(null=True, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82', blank=True)),
                ('mediaforumdemo_date', models.DateTimeField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0')),
            ],
            options={
                'db_table': 'app_mediaforum_demo',
                'verbose_name': '\u041c\u0435\u0434\u0438\u0430 \u0444\u043e\u0440\u0443\u043c',
                'verbose_name_plural': '\u041c\u0435\u0434\u0438\u0430 \u0444\u043e\u0440\u0443\u043c',
            },
            bases=(models.Model,),
        ),
    ]
