# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0099_auto_20150223_0223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('info', models.TextField(max_length=1000, blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Items',
            },
            bases=(models.Model,),
        ),
    ]
