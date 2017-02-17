# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10, null=True, verbose_name='\u59d3\u540d', blank=True)),
                ('age', models.IntegerField(default=0, verbose_name='\u5e74\u9f84')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
