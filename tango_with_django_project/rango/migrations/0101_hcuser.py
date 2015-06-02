# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0100_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='HCUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userID', models.CharField(max_length=200)),
                ('firstName', models.CharField(max_length=200)),
                ('shoppinglist', models.CharField(max_length=2000, blank=True)),
                ('lastSiteVisit', models.CharField(max_length=200, blank=True)),
                ('lastStoreVisit', models.CharField(max_length=200, blank=True)),
            ],
            options={
                'ordering': ['userID'],
                'verbose_name_plural': 'HCUsers',
            },
            bases=(models.Model,),
        ),
    ]
