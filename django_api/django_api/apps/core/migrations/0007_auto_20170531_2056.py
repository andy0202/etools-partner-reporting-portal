# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-31 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_intervention_locations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intervention',
            name='document_type',
            field=models.CharField(blank=True, choices=[('PD', 'Programme Document'), ('SHP', 'Simplified Humanitarian Programme Document'), ('SSF', 'Small-Scale Funding Agreement')], max_length=255, null=True, verbose_name='Document type'),
        ),
    ]