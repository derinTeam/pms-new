from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from . import models
from .forms import ManagerRegisterForms
from .models import ProjectManager
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from project.models import Projects,ProjectDetail,Tasks
from django.contrib.auth.decorators import login_required
from project.forms import ProjectForms,TasksForms
# Create your views here.


def register(request):
    form = ManagerRegisterForms(request.POST or None)
    if form.is_valid():
        company = form.cleaned_data.get("company")
        username = form.cleaned_data.get("username")
        managerFirstName = form.cleaned_data.get("managerFirstName")
        managerLastName = form.cleaned_data.get("managerLastName")
        managerEmail = form.cleaned_data.get("managerEmail")
        managerPassword = form.cleaned_data.get("managerPassword")

        newUser = User(username = username,email = managerEmail)
        newUser.set_password(managerPassword)
        
        newUser.save()

        newManager = ProjectManager(user = newUser,username = username,
            managerFirstName=managerFirstName, managerLastName=managerLastName,
            managerEmail=managerEmail, managerPassword=managerPassword,company = company)
        
        newManager.save()

        login(request,newUser)
        messages.success(request, "Kayıt Başarıyla Gerçekleşti")
        return redirect("index")

    context = {
        "form": form
    }

    return render(request, "manager-register.html", context)

    
@login_required(login_url = "user:loginUser")
def addprojects(request):
    form = ProjectForms(request.POST or None)

    if form.is_valid():

        project = form.save(commit = False)
        project.save()
        form.save_m2m()
        messages.success(request,"Proje Başarılı Bir Şekilde Eklendi")
        return redirect("index")

    return render(request,"addproject.html",{"form":form})

@login_required(login_url = "user:loginUser")
def updateprojects(request,id):

    projects = get_object_or_404(Projects,id = id)
    form = ProjectForms(request.POST or None,instance = projects)

    if form.is_valid():
        projects = form.save(commit = False)
        projects.save()
        form.save_m2m()
        messages.success(request,"Proje Başarılı Bir Şekilde Güncellendi")
        return redirect("project:dashboard")


    return render(request,"project-update.html",{"form":form})

@login_required(login_url = "user:loginUser")
def deleteprojects(request,id):

    projects = get_object_or_404(Projects,id = id)
    projects.delete()
    messages.info(request,"Proje Başarılı Bir Şekilde Silindi")
    return redirect("project:dashboard")
    
@login_required(login_url = "user:loginUser")
def addtask(request):
    form = TasksForms(request.POST or None)
    if form.is_valid():
        task = form.save(commit = False)
        task.save()
        form.save_m2m()
        messages.success(request,"Görev Başarılı Bir Şekilde Eklendi")
        return redirect("project:dashboard")

    return render(request,"task-add.html",{"form":form}) 

@login_required(login_url = "user:loginUser")
def updateTask(request,id):
    task = get_object_or_404(Tasks,id = id)
    form = TasksForms(request.POST or None,instance = task)
    if form.is_valid():
        task = form.save(commit=False)
        task.save()
        form.save_m2m()
        messages.success(request,"Görev Başarılı Bir Şekilde Güncellendi")
        return redirect("project:dashboard")

    return render(request,"task-update.html",{"form":form}) 

@login_required(login_url = "user:loginUser")
def deleteTask(request,id):

    task = get_object_or_404(Tasks,id = id)
    task.delete()
    messages.info(request,"Görev Silindi")
    return redirect("project:dashboard")
