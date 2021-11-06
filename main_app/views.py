from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from .models import Project

from django.shortcuts import render, redirect, reverse


# Create your views here.

class Home(TemplateView):
    template_name = "home.html"


class ProjectList(TemplateView):
    template_name = "project_list.html"
class ProjectDetail(DetailView):
    model = Project
    template_name = "project_detail.html"
    