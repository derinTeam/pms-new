from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProjectForms
from .models import Projects, ProjectDetail, Tasks ,Comment
from employee.models import Employee
from p_manager.models import ProjectManager

# Create your views here.


def index(request):
    return render(request, "index.html")


@login_required(login_url="user:loginUser")
def dashboard(request):
    content = {}
    projectManager = ProjectManager.objects.filter(user=request.user)
    if projectManager:
        projects = Projects.objects.filter(
            projectManager=ProjectManager.objects.get(user=request.user))
        tasks = Tasks.objects.filter(
            tasksManager=ProjectManager.objects.get(user=request.user))
        content = {
            "projects": projects,
                "projectManager": projectManager,
                "tasks": tasks
        }
    else:
        employee = Employee.objects.filter(user=request.user)
        if employee:
            projects = Projects.objects.filter(
                employees=Employee.objects.get(user=request.user))
            tasks = Tasks.objects.filter(
                employees=Employee.objects.get(user=request.user))
            
            content = {
                "projects": projects,
                "employee": employee,
                "tasks": tasks
            }

    return render(request, "dashboard.html",content)

def projectsPage(request):
    projects = Projects.objects.all()
    keyword = request.GET.get("keyword")

    if keyword:
        projects = Projects.objects.filter(title__contains = keyword)
        return render(request,"projects.html",{"all_projects":projects})


    return render(request,"projects.html",{"all_projects":projects})



def projectDetail(request,id):
    
    project = get_object_or_404(Projects,id = id)
    comments = project.comments.all()
    context = {
        "project" : project,
        "comments" : comments
    }

    return render(request,"project-detail.html",context)

def addComment(request,id):
    project = get_object_or_404(Projects,id = id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newCommnet = Comment(comment_author = comment_author, comment_content = comment_content)

        newCommnet.project = project

        newCommnet.save()

    return redirect(reverse("project:projectDetail",kwargs={"id":id}))