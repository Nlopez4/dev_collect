# Generated by Django 3.2.9 on 2021-11-08 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='user',
        ),
    ]
