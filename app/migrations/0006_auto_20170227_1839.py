# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, upload_to='static/img/book_photos'),
        ),
    ]