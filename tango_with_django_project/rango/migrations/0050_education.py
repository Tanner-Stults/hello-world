# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rango', '0049_auto_20141222_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school', models.CharField(max_length=200)),
                ('degree', models.CharField(max_length=200)),
                ('major', models.CharField(max_length=200, blank=True)),
                ('minor', models.CharField(max_length=200, blank=True)),
                ('startDate', models.DateField(default=datetime.date.today)),
                ('endDate', models.DateField(default=datetime.date.today)),
                ('grade', models.CharField(max_length=100, blank=True)),
                ('info', models.CharField(max_length=1000, blank=True)),
                ('activities', models.CharField(max_length=1000, blank=True)),
                ('user', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
