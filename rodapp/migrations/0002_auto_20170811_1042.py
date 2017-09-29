# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 10:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rodapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prediction',
            name='algorithm',
        ),
        migrations.RemoveField(
            model_name='prediction',
            name='feature',
        ),
        migrations.RemoveField(
            model_name='prediction',
            name='symbol',
        ),
        migrations.RemoveField(
            model_name='prediction',
            name='user',
        ),
        migrations.DeleteModel(
            name='Algorithm',
        ),
        migrations.DeleteModel(
            name='Feature',
        ),
        migrations.DeleteModel(
            name='Prediction',
        ),
        migrations.DeleteModel(
            name='Symbol',
        ),
    ]