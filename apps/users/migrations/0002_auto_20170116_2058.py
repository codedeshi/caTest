# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 02:58
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='permission_level',
        ),
        migrations.AlterField(
            model_name='user',
            name='auth_Token',
            field=models.CharField(default=uuid.uuid4, max_length=36),
        ),
    ]
