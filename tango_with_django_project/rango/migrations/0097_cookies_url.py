# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0096_cookies'),
    ]

    operations = [
        migrations.AddField(
            model_name='cookies',
            name='url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
