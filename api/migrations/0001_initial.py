# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-22 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='店名')),
                ('description', models.TextField(verbose_name='説明')),
                ('address', models.CharField(max_length=256, verbose_name='住所')),
                ('lat', models.IntegerField(verbose_name='緯度')),
                ('lng', models.IntegerField(verbose_name='経度')),
            ],
        ),
    ]
