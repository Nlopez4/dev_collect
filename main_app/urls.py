from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),  # splash page


    # Post Project
    path('project/', views.ProjectList.as_view(),name="project_list"),
    path('project/<int:pk>/', views.ProjectDetail.as_view(), name="project_detail"),
    #path('project/new/', views.createProject, name="project_create"),
    path('project/new/', views.ProjectCreate.as_view(  ), name="project_create"),
]
