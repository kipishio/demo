# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_auto_20150908_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaForumDemo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='mediademo',
            old_name='mediademo_opisanie',
            new_name='mediademo_tema',
        ),
    ]
