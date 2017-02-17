# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160715_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='boy',
            name='y',
            field=models.IntegerField(default=0, verbose_name='y\u5750\u6807'),
            preserve_default=True,
        ),
    ]
