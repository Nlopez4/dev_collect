from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.Home.as_view(), name="home"),  # splash page
    # AUTH
     path('registration/signup/', views.Signup.as_view(), name="signup"),
   
    
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

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)