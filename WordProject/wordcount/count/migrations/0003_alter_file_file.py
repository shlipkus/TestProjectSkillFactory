# Generated by Django 5.0.6 on 2024-05-21 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('count', '0002_file_word'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(max_length=255, null=True, upload_to='files/'),
        ),
    ]
