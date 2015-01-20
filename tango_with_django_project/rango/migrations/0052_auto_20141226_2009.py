# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0051_auto_20141222_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='school',
            field=models.CharField(max_length=200, choices=[(b'1', b'Ph. D'), (b'2', b'BA'), (b'3', b'BS'), (b'4', b"Master's")]),
        ),
        migrations.AlterField(
            model_name='education',
            name='schoolType',
            field=models.CharField(max_length=200, choices=[(b'1', b'High School'), (b'2', b'Community College'), (b'3', b'College'), (b'4', b'Technical Institute')]),
        ),
        migrations.AlterField(
            model_name='education',
            name='user',
            field=models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
