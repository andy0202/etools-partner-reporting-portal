# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-01 19:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0002_auto_20170527_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partneractivity',
            name='cluster_activity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partner_activities', to='cluster.ClusterActivity'),
        ),
    ]