from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    image = models.FileField(blank=True, null=True, upload_to='profile/')
    email = models.EmailField(max_length=500)
    bio = models.TextField(max_length=3000)
    github = models.CharField(max_length=2000, null=True, blank=True)
    skills = models.CharField(max_length=500)

    def __str__(self):
        return str(self.user)


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    skills = models.CharField(max_length=500)
    github_link = models.CharField(max_length=2000, null=True, blank=True)
    site_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title


