# Generated by Django 3.2.9 on 2021-11-11 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_project_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default.jpeg', null=True, upload_to='profile/'),
        ),
    ]
