# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0065_auto_20150108_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(max_length=200, choices=[(b'1', b'Ph. D'), (b'2', b'BA'), (b'3', b'BS'), (b'4', b"Master's"), (b'5', b'AA')]),
        ),
    ]
