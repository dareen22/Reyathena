# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=50)),
                ('level', models.CharField(max_length=50)),
                ('age', models.IntegerField(null=True, blank=True)),
                ('budget', models.FloatField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('link', models.URLField(null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='athlete',
            name='type',
            field=models.ForeignKey(blank=True, to='app.Sport', null=True),
        ),
    ]
