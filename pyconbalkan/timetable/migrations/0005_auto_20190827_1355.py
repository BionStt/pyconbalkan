# Generated by Django 2.2.4 on 2019-08-27 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0004_presentation_conference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='speaker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='presentations', to='speaker.Speaker'),
        ),
    ]
