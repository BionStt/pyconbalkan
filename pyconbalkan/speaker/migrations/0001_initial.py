# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-26 21:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50)),
                ('job', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SpeakerPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(upload_to='static/img')),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='speaker.Speaker')),
            ],
        ),
    ]
