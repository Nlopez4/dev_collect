from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile, Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'skills', 'github_link', 'site_link']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'skills': forms.TextInput(attrs={'class': 'form-control'}),
            'github_link': forms.TextInput(attrs={'class': 'form-control'}),
            'site_link': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'image', 'email', 'bio', 'github', 'skills')

    widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'skills': forms.TextInput(attrs={'class': 'form-control'}),
            'github_link': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
    
    
class CreateForm(forms.ModelForm):
    class Meta: Project 
    fields = ['title', 'description', 'skills', 'github_link', 'site_link']
    
    widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'skills': forms.TextInput(attrs={'class': 'form-control'}),
            'github_link': forms.TextInput(attrs={'class': 'form-control'}),
            
        }