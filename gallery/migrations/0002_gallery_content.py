# Generated by Django 3.2.16 on 2024-01-15 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]