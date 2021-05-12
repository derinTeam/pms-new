from django.contrib import admin
from .models import ProjectManager
from .models import Company
# Register your models here.

@admin.register(ProjectManager)
class ProjectManagerAdmin(admin.ModelAdmin):

    list_display = ["user","managerFirstName","managerLastName", "managerEmail","username"]
    list_display_links = ["user","managerFirstName","managerLastName", "managerEmail"]
    search_fields = ["managerFirstName"]
    list_filter = ["managerFirstName"]
    class Meta:
        model = ProjectManager

@admin.register(Company)
class Company(admin.ModelAdmin):

    list_display = ["social_name","name", "email","city"]
    list_display_links = ["social_name","name", "email"]
    search_fields = ["social_name"]
    list_filter = ["social_name"]
    class Meta:
        model = Company        