# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-08-07 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20190806_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.CharField(default=0.0, max_length=40),
        ),
    ]
