# Generated by Django 2.0.5 on 2018-06-03 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizers', '0002_remove_volunteer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteerphoto',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='organizers/volunteer/profile_picture'),
        ),
    ]
