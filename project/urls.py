from django.contrib import admin
from django.urls import path
from . import views


app_name = "project"

urlpatterns = [
    #path('projectdetail/<int:id>',views.projectdetail,name = "projectdetail"),
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('projects/',views.projectsPage,name = "projects")
]