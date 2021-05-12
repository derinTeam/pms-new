from django.contrib import admin

from .models import Employee
# Register your models here.
@admin.register(Employee)
class ProjectsAdmin(admin.ModelAdmin):

    list_display = ["employeeFirstName","employeeLastName","employeeEmail","username"]
    list_display_links = ["employeeFirstName","employeeEmail"]
    search_fields = ["employeeFirstName"]
    list_filter = ["employeeFirstName"]
    class Meta:
        model = Employee