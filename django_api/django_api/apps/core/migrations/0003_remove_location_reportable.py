# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-19 00:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170918_2336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='reportable',
        ),
    ]
