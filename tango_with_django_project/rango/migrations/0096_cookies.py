# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0095_auto_20150122_2303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cookies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=2000)),
                ('domain', models.CharField(max_length=2000, blank=True)),
                ('name', models.CharField(max_length=2000, blank=True)),
                ('content', models.CharField(max_length=2000, blank=True)),
                ('path', models.CharField(max_length=2000, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
