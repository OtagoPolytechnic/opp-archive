# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='students',
            field=models.ManyToManyField(to='archive.Student'),
        ),
    ]
