# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boy',
            name='birthday',
            field=models.DateTimeField(null=True, verbose_name='\u51fa\u751f\u65e5\u671f', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='boy',
            name='home',
            field=models.CharField(verbose_name='\u5bb6', max_length=50, null=True, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='boy',
            name='is_new',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u65b0\u6765'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='boy',
            name='like',
            field=models.CharField(max_length=20, null=True, verbose_name='\u7231\u597d', blank=True),
            preserve_default=True,
        ),
    ]
