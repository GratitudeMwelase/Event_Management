# Generated by Django 5.2.3 on 2025-06-25 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
