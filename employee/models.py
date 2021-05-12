from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, verbose_name="Kullanıcı Adı")
    employeeFirstName = models.CharField(
        max_length=50, verbose_name="Çalışan İsmi")
    employeeLastName = models.CharField(
        max_length=50, verbose_name="Çalışan Soyismi")
    employeeEmail = models.EmailField(
        max_length=120, verbose_name="Çalışan Mail Adresi")
    employeePassword = models.CharField(
        max_length=50, verbose_name="Çalışan Parola")

    def __str__(self):
        return self.employeeFirstName + " " + self.employeeLastName
