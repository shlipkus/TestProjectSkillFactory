# Generated by Django 5.0.6 on 2024-05-21 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('count', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='word',
            field=models.CharField(default=' ', max_length=128),
        ),
    ]
