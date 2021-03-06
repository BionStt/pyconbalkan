# Generated by Django 2.2.4 on 2019-08-29 10:56

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('speaker', '0013_remove_speaker_keynote'),
    ]

    operations = [
        migrations.CreateModel(
            name='YouTubeLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', embed_video.fields.EmbedVideoField()),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='speaker.Speaker')),
            ],
        ),
    ]
