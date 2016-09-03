# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20160902_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
