from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Project, Profile
from .forms import ProjectForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from django.shortcuts import render, redirect, reverse


class Home(TemplateView):
    template_name = "home.html"


class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit validate the form and login the user.

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("project_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)


# Profile
@method_decorator(login_required, name='dispatch')
class ProfilePage(TemplateView):
    model = Profile
    template_name = "profile.html"
    ordering = ['created_at']

    def get_context_data(self, pk, **kwargs):
        profile = Profile.objects.get(pk=pk)
        context = super().get_context_data(**kwargs)
        context["profile"] = profile
        context["projects"] = Profile.objects.filter(user=self.request.user)
        return context


@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "profile_update.html"

    def updateProfile(request):
        form = ProfileForm()
        if request.method == "POST":
            form = ProfileUpdate(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})

# CRUD for Project


@method_decorator(login_required, name='dispatch')
class ProjectCreate(CreateView):
    model = Project
    form_class = ProfileForm
    # fields = ['title', 'description', 'skills', 'github_link', 'site_link']
    template_name = "project_create.html"
    success_url = "/project/"

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super(ProjectCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('project_list')


@method_decorator(login_required, name='dispatch')
class ProjectUpdate(UpdateView):
    model = Project
    form_class = ProjectForm
    # fields = ['title', 'description', 'skills', 'github_link', 'site_link']
    template_name = "project_update.html"
    success_url = "/project/"

def project_update(pk, request):
        profile = request.user.profile
        project = profile.project_set.get(pk=pk)


@method_decorator(login_required, name='dispatch')
class ProjectDelete(DeleteView):
    model = Project
    template_name = "project_delete_confirmation.html"
    success_url = "/project/"

def project_delete(pk, request):
        profile = request.user.profile
        project = profile.project_set.get(pk=pk)

def get_success_url(self):
    return reverse('project', kwargs={'pk': self.request.user.pk})

# PROJECT


@method_decorator(login_required, name='dispatch')
class ProjectList(TemplateView):
    template_name = "project_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title")

        if title != None:
            context["projects"] = Project.objects.filter(title__icontains=title)
        else:
            context["projects"] = Project.objects.all()
        return context


@method_decorator(login_required, name='dispatch')
class ProjectDetail(DetailView):
    model = Project
    template_name = "project_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all()
        return context
