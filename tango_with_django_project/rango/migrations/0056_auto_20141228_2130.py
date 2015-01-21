# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0055_auto_20141227_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name=b'cropping',
            field=image_cropping.fields.ImageRatioField(b'picture', '255x300', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='cropping'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=image_cropping.fields.ImageCropField(null=True, upload_to=b'profile_images', blank=True),
        ),
    ]
