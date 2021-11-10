from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Project
from .forms import ProjectForm


from django.shortcuts import render, redirect, reverse


# Create your views here.

class Home(TemplateView):
    template_name = "home.html"



# CRUD
class ProjectCreate(CreateView):
    model = Project
    fields = ['title', 'description', 'skills', 'github_link', 'site_link']
    template_name = "project_create.html"
    success_url = "/project/"
    
    def form_valid(self, form):
        return super(ProjectCreate, self).form_valid(form)
    
    def get_success_url(self):
        print(self.kwargs)
        return reverse('project_list')

class ProjectUpdate(UpdateView):
    model = Project
    fields = ['title', 'description', 'skills', 'github_link', 'site_link']
    template_name = "project_update.html"
    success_url = "/project/"

class ProjectDelete(DeleteView):
    model = Project
    template_name = "project_delete_confirmation.html"
    success_url = "/project/"



# PROJECT
class ProjectList(TemplateView):
    template_name = "project_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all() 
        return context


class ProjectDetail(DetailView):
    model = Project
    template_name = "project_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all() 
        return context


    

