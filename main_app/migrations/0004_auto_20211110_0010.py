# Generated by Django 3.2.9 on 2021-11-10 00:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0003_project_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='tech_used',
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.FileField(blank=True, null=True, upload_to='profile/')),
                ('email', models.EmailField(max_length=500)),
                ('bio', models.CharField(max_length=1000)),
                ('github', models.CharField(blank=True, max_length=2000, null=True)),
                ('skills', models.ManyToManyField(blank=True, to='main_app.Skills')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='skills',
            field=models.ManyToManyField(blank=True, to='main_app.Skills'),
        ),
    ]
