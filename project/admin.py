from django.contrib import admin

from .models import Projects, ProjectDetail, Tasks
# Register your models here.


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):

    list_display = ["projectName", "created_date"]
    list_display_links = ["projectName", "created_date"]
    search_fields = ["projectName"]
    list_filter = ["created_date"]

    class Meta:
        model = Projects


@admin.register(ProjectDetail)
class ProjectDetail(admin.ModelAdmin):
    list_display = ["projectEmployee", "projectName"]
    list_display_links = ["projectEmployee", "projectName"]
    search_fields = ["projectEmployee", "projectName"]
    list_filter = ["projectEmployee", "projectName"]

    class Meta:
        model = ProjectDetail


@admin.register(Tasks)
class Tasks(admin.ModelAdmin):
    list_display = ["project",
                    "task_name", "status",
                    "due","created_date","update_date"]
    list_display_links = ["project"]
    search_fields = ["task_name", "status"]
    list_filter = ["project", "due"]

    class Meta:
        model = Tasks
