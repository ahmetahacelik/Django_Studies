# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-20 10:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Budget', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Age', models.IntegerField()),
                ('CurrentProject', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Lab.Project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='Workers',
            field=models.ManyToManyField(blank=True, to='Lab.Worker'),
        ),
    ]