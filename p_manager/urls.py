from django.contrib import admin
from django.urls import path
from . import views

app_name = "p_manager"

urlpatterns = [
    path('register/',views.register,name = "register"),
    path('addprojects/',views.addprojects,name = "addprojects"),
    path('updateprojects/<int:id>',views.updateprojects,name = "updateprojects"),
    path('deleteprojects/<int:id>',views.deleteprojects,name = "deleteprojects"),
    path('addtask/',views.addtask,name = "addtask")
]