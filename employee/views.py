from django.shortcuts import render, redirect, render, HttpResponse, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import EmployeeRegisterForm
from project.forms import StatusDueUpdate
from .models import Employee
from project.models import Tasks
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):

    form = EmployeeRegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        employeeFirstName = form.cleaned_data.get("employeeFirstName")
        employeeLastName = form.cleaned_data.get("employeeLastName")
        employeeEmail = form.cleaned_data.get("employeeEmail")
        employeePassword = form.cleaned_data.get("employeePassword")

        newUser = User(username=username, email=employeeEmail)
        newUser.set_password(employeePassword)
        newUser.save()

        newEmployee = Employee(user=newUser, username=username,
                               employeeFirstName=employeeFirstName, employeeLastName=employeeLastName,
                               employeeEmail=employeeEmail, employeePassword=employeePassword
                               )

        newEmployee.save()

        login(request, newUser)

        messages.success(request, "Kayıt Başarıyla Gerçekleşti")
        return redirect("index")

    context = {
        "form": form
    }

    return render(request, "employee-register.html", context)


def taskUpdateStatus(id):
    
    task = Tasks.objects.get(id = id)
    if task.status == "1":
        task.status = "2"
    elif task.status == "2":
        task.status = "3"
    elif task.status == "3":
        task.status = "1"        
    return task.status            


def taskUpdateDue(id):
   
    task = Tasks.objects.get(id = id)
    if task.due == "1":
        task.due = "2"
    elif task.due == "2":
        task.due = "3"
    elif task.due == "3":
        task.due = "1"   
    return task.due            


def updatestatus(request,id):

    task = get_object_or_404(Tasks,id = id)
    task.status = taskUpdateStatus(task.id)
    task.save()
    messages.info(request,"Durum Başarılı Bir Şekilde Güncellendi")
    return redirect("project:dashboard")

def updatedue(request,id):

    task = get_object_or_404(Tasks,id = id)
    task.due = taskUpdateDue(task.id)
    task.save()
    messages.info(request,"Zaman Durumu Başarılı Bir Şekilde Güncellendi")
    return redirect("project:dashboard")