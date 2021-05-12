from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from p_manager.models import ProjectManager
from employee.models import Employee
# Create your views here.


@login_required(login_url="user:loginUser")
def logoutUser(request):
    logout(request)
    messages.success(request, "Çıkış Yapıldı")
    return redirect("index")


def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        if user is None:
            messages.info(request, "Mail Adresi Veya Şifre Hatalı")
            return render(request, "login.html", context)

        messages.info(request, "Başarılı Giriş")
        login(request, user)
        return redirect("index")
    return render(request, "login.html", context)


def userclaim(request):
    context = {}
    projectManager = ProjectManager.objects.filter(user=request.user)
    if projectManager:
        context = {
            "projectManager": projectManager
        }

    else:
        employee = Employee.objects.filter(user=request.user)
        if employee:
            context = {
                "employee": employee
            }

    return render(request,"navbar.html",context)