from django import forms
from django.db.models import fields
from .models import Projects, ProjectDetail, Tasks, ManagerEmployees,ProjectDocument


class ProjectForms(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ["projectName", "projectStatus",
                  "projectPoint", "projectManager",
                   "employees", "efforts", "dead_line",
                    "company", "complete_per", "description"]


class ProjectDetailForms(forms.ModelForm):
    class Meta:
        model = ProjectDetail
        fields = ["projectEmployee", "projectName"]


class TasksForms(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ["tasksManager","project", "employees",
                  "task_name", "status",
                  "due"]


class ManagerEmployees(forms.ModelForm):
    class Meta:
        model = ManagerEmployees
        fields = ["managers", "employee"]

class StatusDueUpdate(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ["status","due"]


class ProjectDocumentForm(forms.ModelForm):
    class Meta:
        model = ProjectDocument
        fields = ["project","document"]        