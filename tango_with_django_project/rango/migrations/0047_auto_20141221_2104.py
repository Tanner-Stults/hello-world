# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0046_auto_20141221_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='firstName',
            field=models.CharField(default=b'Joe', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='lastName',
            field=models.CharField(default=b'Shmo', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(editable=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
