from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),  # splash page
    # AUTH
   
    
    # Profile
    path('profile/<int:pk>/', views.ProfilePage.as_view(), name="profile"),
    path('profile/<int:pk>/update', views.ProfileUpdate.as_view(), name="profile_update"),

    # Post Project
    path('project/', views.ProjectList.as_view(),name="project_list"),
    path('project/<int:pk>/', views.ProjectDetail.as_view(), name="project_detail"),
    path('project/new/', views.ProjectCreate.as_view(  ), name="project_create"),
    path('project/<int:pk>/update', views.ProjectUpdate.as_view(), name="project_update"),
    path('project/<int:pk>/delete', views.ProjectDelete.as_view(), name="project_delete"),
]
