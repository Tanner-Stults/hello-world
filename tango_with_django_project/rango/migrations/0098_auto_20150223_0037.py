# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0097_cookies_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cookies',
            name='url',
            field=models.CharField(max_length=20000),
        ),
    ]
