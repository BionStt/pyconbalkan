# Generated by Django 2.1.7 on 2019-03-03 16:55

from django.db import migrations, models
import django.db.models.deletion
import pyconbalkan.conference.abstractions


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0007_auto_20190227_0738'),
        ('news', '0007_auto_20180801_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='conference',
            field=models.ForeignKey(default=pyconbalkan.conference.abstractions._get_default_conference, on_delete=django.db.models.deletion.CASCADE, to='conference.Conference'),
        ),
    ]
