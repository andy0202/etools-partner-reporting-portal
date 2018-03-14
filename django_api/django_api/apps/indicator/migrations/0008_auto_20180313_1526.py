# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-13 15:26
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180313_1046'),
        ('indicator', '0007_auto_20180305_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportableLocationGoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('target', django.contrib.postgres.fields.jsonb.JSONField(default={'c': 0, 'd': 0, 'v': 0})),
                ('baseline', django.contrib.postgres.fields.jsonb.JSONField(default={'c': 0, 'd': 0, 'v': 0})),
                ('in_need', django.contrib.postgres.fields.jsonb.JSONField(default={'c': 0, 'd': 0, 'v': 0})),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Location')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='reportable',
            name='contributes_to_partner',
            field=models.BooleanField(default=False),
        ),
        migrations.RemoveField(
            model_name='reportable',
            name='locations',
        ),
        migrations.AddField(
            model_name='reportable',
            name='locations',
            field=models.ManyToManyField(related_name='reportables', through='indicator.ReportableLocationGoal', to='core.Location'),
        ),
        migrations.AddField(
            model_name='reportablelocationgoal',
            name='reportable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicator.Reportable'),
        ),
    ]
