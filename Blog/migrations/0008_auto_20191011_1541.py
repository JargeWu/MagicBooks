# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-11 15:41
from __future__ import unicode_literals

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_article_contents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='contents',
            field=mdeditor.fields.MDTextField(null=True),
        ),
    ]