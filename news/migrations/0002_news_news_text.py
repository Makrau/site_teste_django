# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-14 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_text',
            field=models.TextField(default='Notícia Invalida!'),
        ),
    ]
