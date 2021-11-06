from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from .models import Project

from django.shortcuts import render, redirect, reverse


# Create your views here.

class Home(TemplateView):
    template_name = "home.html"


# Project
class ProjectList(TemplateView):
    template_name = "project_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all() # Here we are using the model to query the database for us.
        return context


class ProjectDetail(DetailView):
    model = Project
    template_name = "project_detail.html"


