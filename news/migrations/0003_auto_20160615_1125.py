# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-15 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_news_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='caption',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_text',
            field=models.TextField(default='Preencha aqui sua notícia!'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.TextField(max_length=100),
        ),
    ]
