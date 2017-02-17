# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_boy_y'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Boy',
        ),
        migrations.CreateModel(
            name='OaActivitys',
            fields=[
            ],
            options={
                'db_table': 'oa_activitys',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OaAdmin',
            fields=[
            ],
            options={
                'db_table': 'oa_admin',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OaFetchcompany',
            fields=[
            ],
            options={
                'db_table': 'oa_fetchcompany',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OaFetchpeople',
            fields=[
            ],
            options={
                'db_table': 'oa_fetchpeople',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OaFiles',
            fields=[
            ],
            options={
                'db_table': 'oa_files',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OaFilesDiscuss',
            fields=[
            ],
            options={
                'db_table': 'oa_files_discuss',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
