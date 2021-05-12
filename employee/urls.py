from django.contrib import admin
from django.urls import path
from . import views

app_name = "employee"

urlpatterns = [
    path('register/',views.register,name = "register"),
    path('updatestatus/<int:id>',views.updatestatus,name = "updatestatus"),
    path('updatedue/<int:id>',views.updatedue,name = "updatedue"),
    
]