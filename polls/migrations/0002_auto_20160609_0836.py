# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='description',
            field=models.TextField(),
        ),
    ]
