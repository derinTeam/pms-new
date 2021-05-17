from django.contrib import admin
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('logout/',views.logoutUser,name = "logoutUser"),
    path('login/',views.loginUser,name = "loginUser"),
    
]