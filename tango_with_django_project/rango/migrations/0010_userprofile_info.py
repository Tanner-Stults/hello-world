# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0009_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='info',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
