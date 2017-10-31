# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-30 17:12
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=models.CharField(max_length=100))),
                ('logo', models.ImageField(default=None, upload_to=b'')),
                ('details', models.TextField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=models.CharField(max_length=100))),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('img1', models.ImageField(default=None, upload_to=b'')),
                ('img2', models.ImageField(default=None, upload_to=b'')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pottery.Brand')),
            ],
        ),
    ]
