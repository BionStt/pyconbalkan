# Generated by Django 2.1.7 on 2019-02-27 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0006_conference_timetable_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='year',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
