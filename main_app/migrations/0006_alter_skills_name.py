# Generated by Django 3.2.9 on 2021-11-10 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='name',
            field=models.CharField(max_length=500),
        ),
    ]