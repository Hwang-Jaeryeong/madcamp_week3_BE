# Generated by Django 3.2.16 on 2024-01-15 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peoples', '0003_alter_person_picture_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='picture_url',
            field=models.ImageField(blank=True, null=True, upload_to='person_images/'),
        ),
    ]
