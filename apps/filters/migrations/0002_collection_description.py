# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='description',
            field=models.TextField(default='None', verbose_name='Description'),
        ),
    ]
