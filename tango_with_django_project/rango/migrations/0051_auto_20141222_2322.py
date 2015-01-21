# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0050_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='schoolType',
            field=models.CharField(default='College', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='education',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
