from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from .models import Project
from .forms import ProjectForm


from django.shortcuts import render, redirect, reverse


# Create your views here.

class Home(TemplateView):
    template_name = "home.html"


# Project
# class ProjectCreate(CreateView):
#     model = Project
#     fields = ['user', 'title', 'description', 'tech_used', 'github_link', 'site_link']
#     template_name = "project_create.html"
#     success_url = "/project/"

def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    
    context = {'form': form}
    return render(request, "project_create.html", context)
    
class ProjectList(TemplateView):
    template_name = "project_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all() # Here we are using the model to query the database for us.
        return context


class ProjectDetail(DetailView):
    model = Project
    template_name = "project_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all() 
        return context


    

