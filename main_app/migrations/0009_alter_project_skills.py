# Generated by Django 3.2.9 on 2021-11-10 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20211110_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='skills',
            field=models.TextField(max_length=300),
        ),
    ]
