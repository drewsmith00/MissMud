# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-02 10:57
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pottery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name'),
        ),
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name'),
        ),
    ]