# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-13 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cluster', '0005_remove_clusteractivity_standard'),
    ]

    operations = [
        migrations.AddField(
            model_name='cluster',
            name='external_id',
            field=models.CharField(blank=True, help_text='An ID representing this instance in an external system', max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='cluster',
            name='external_source',
            field=models.TextField(blank=True, choices=[('HPC', 'HPC'), ('OPS', 'OPS')], null=True),
        ),
        migrations.AddField(
            model_name='cluster',
            name='imported_type',
            field=models.TextField(blank=True, help_text='Type as specified in the external system', max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='clusteractivity',
            name='external_id',
            field=models.CharField(blank=True, help_text='An ID representing this instance in an external system', max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='clusteractivity',
            name='external_source',
            field=models.TextField(blank=True, choices=[('HPC', 'HPC'), ('OPS', 'OPS')], null=True),
        ),
        migrations.AddField(
            model_name='clusterobjective',
            name='external_id',
            field=models.CharField(blank=True, help_text='An ID representing this instance in an external system', max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='clusterobjective',
            name='external_source',
            field=models.TextField(blank=True, choices=[('HPC', 'HPC'), ('OPS', 'OPS')], null=True),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='type',
            field=models.CharField(choices=[('cccm', 'CCCM'), ('early_recovery', 'Early Recovery'), ('education', 'Education'), ('emergency_telecommunications', 'Emergency Telecommunications'), ('food_security', 'Food Security'), ('health', 'Health'), ('logistics', 'Logistics'), ('nutrition', 'Nutrition'), ('protection', 'Protection'), ('shelter', 'Shelter'), ('wash', 'WASH'), ('imported', 'Imported')], max_length=32),
        ),
        migrations.AlterField(
            model_name='clusteractivity',
            name='title',
            field=models.TextField(max_length=2048),
        ),
        migrations.AlterField(
            model_name='clusterobjective',
            name='title',
            field=models.TextField(max_length=2048, verbose_name='Cluster Objective Title'),
        ),
        migrations.AlterUniqueTogether(
            name='cluster',
            unique_together=set([('external_id', 'external_source'), ('type', 'imported_type', 'response_plan')]),
        ),
        migrations.AlterUniqueTogether(
            name='clusteractivity',
            unique_together=set([('external_id', 'external_source')]),
        ),
        migrations.AlterUniqueTogether(
            name='clusterobjective',
            unique_together=set([('external_id', 'external_source')]),
        ),
    ]