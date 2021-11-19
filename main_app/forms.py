from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile, Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'skills', 'github_link', 'site_link']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-4 w-25 p-3 justify-content-center'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-4 w-25 p-3'}),
            'skills': forms.TextInput(attrs={'class': 'form-control mb-4 w-25 p-3'}),
            'github_link': forms.TextInput(attrs={'class': 'form-control mb-4 w-25 p-3'}),
            'site_link': forms.TextInput(attrs={'class': 'form-control mb-4 w-25 p-3'}),
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'image', 'email', 'bio', 'github', 'skills')
