# Generated by Django 3.2.16 on 2024-01-15 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peoples', '0002_alter_person_picture_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='picture_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]