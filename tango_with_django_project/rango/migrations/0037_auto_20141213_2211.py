# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rango', '0036_workexperience'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkExperience2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=1000)),
                ('jobTitle', models.CharField(max_length=1000)),
                ('location', models.CharField(max_length=1000)),
                ('startDate', models.DateTimeField(default=datetime.datetime.now)),
                ('endDate', models.DateTimeField(default=datetime.datetime.now)),
                ('info', models.CharField(max_length=1000)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='user',
        ),
        migrations.DeleteModel(
            name='WorkExperience',
        ),
    ]
