from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile, Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'skills', 'github_link', 'site_link']
        
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'email', 'bio', 'github', 'skills')