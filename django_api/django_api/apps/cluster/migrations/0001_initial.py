# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-11 23:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('external_id', models.CharField(blank=True, help_text='An ID representing this instance in an external system', max_length=32, null=True)),
                ('external_source', models.TextField(blank=True, choices=[('HPC', 'HPC'), ('OPS', 'OPS')], null=True)),
                ('type', models.CharField(choices=[('cccm', 'CCCM'), ('early_recovery', 'Early Recovery'), ('education', 'Education'), ('emergency_telecommunications', 'Emergency Telecommunications'), ('food_security', 'Food Security'), ('health', 'Health'), ('logistics', 'Logistics'), ('nutrition', 'Nutrition'), ('protection', 'Protection'), ('shelter', 'Shelter'), ('wash', 'WASH'), ('imported', 'Imported')], max_length=32)),
                ('imported_type', models.TextField(blank=True, help_text='Type as specified in the external system', max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClusterActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('external_id', models.CharField(blank=True, help_text='An ID representing this instance in an external system', max_length=32, null=True)),
                ('external_source', models.TextField(blank=True, choices=[('HPC', 'HPC'), ('OPS', 'OPS')], null=True)),
                ('title', models.TextField(max_length=2048)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ClusterObjective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('external_id', models.CharField(blank=True, help_text='An ID representing this instance in an external system', max_length=32, null=True)),
                ('external_source', models.TextField(blank=True, choices=[('HPC', 'HPC'), ('OPS', 'OPS')], null=True)),
                ('title', models.TextField(max_length=2048, verbose_name='Cluster Objective Title')),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cluster_objectives', to='cluster.Cluster')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
