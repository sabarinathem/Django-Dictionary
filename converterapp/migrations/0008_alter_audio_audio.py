# Generated by Django 3.2.8 on 2021-10-16 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converterapp', '0007_alter_audio_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='audio',
            field=models.FileField(null=True, upload_to='audio/'),
        ),
    ]
