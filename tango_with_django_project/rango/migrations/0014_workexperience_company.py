# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0013_workexperience'),
    ]

    operations = [
        migrations.AddField(
            model_name='workexperience',
            name='company',
            field=models.CharField(default='wanderu', max_length=1000),
            preserve_default=False,
        ),
    ]
