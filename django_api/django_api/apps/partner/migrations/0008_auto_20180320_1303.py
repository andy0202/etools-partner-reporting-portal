# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-20 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0007_auto_20180306_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partnerproject',
            name='description',
            field=models.TextField(max_length=5120),
        ),
    ]