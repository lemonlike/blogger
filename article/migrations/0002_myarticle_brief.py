# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-25 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myarticle',
            name='brief',
            field=models.TextField(blank=True, null=True, verbose_name='\u6587\u7ae0\u7b80\u4ecb'),
        ),
    ]
