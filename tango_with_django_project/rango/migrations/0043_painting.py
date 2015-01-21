# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0042_auto_20141213_2230'),
    ]

    operations = [
        migrations.CreateModel(
            name='painting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, blank=True)),
                ('date', models.DateField(blank=True)),
                ('location', models.CharField(max_length=200, blank=True)),
                ('medium', models.ImageField(default=b'/Users/Tanner_Stults/Desktop/Django/git/tango_with_django_project/media/profile_bgimages/default.jpg', upload_to=b'paintings', blank=True)),
                ('info', models.CharField(max_length=2000, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
