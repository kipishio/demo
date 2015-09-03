# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Onesite_Demo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('onesitedemo_titel', models.CharField(max_length=200)),
                ('onesitedemo_text', models.TextField()),
                ('onesitedemo_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'app_onesite_demo',
            },
            bases=(models.Model,),
        ),
    ]
