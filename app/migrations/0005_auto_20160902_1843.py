# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20160902_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='image',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='athlete',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
