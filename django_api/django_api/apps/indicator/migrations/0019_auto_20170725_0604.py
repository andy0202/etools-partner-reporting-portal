# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-25 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicator', '0018_auto_20170718_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicatorreport',
            name='time_period_start',
            field=models.DateField(),
        ),
    ]
