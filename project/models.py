from django.db import models
from p_manager.models import ProjectManager
from employee.models import Employee
from p_manager.models import Company
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
status = (
    ('1', 'Durdu'),
    ('2', 'Çalışıyor'),
    ('3', 'Bitti'),
)

due = (
    ('1', 'Zamanı Yaklaşıyor'),
    ('2', 'Zamanı Aştı'),
    ('3', 'Bitti'),
)


class Projects(models.Model):

    projectManager = models.ForeignKey(
        ProjectManager, on_delete=models.CASCADE, verbose_name="Projenin Yöneticisi")
    projectName = models.CharField(max_length=100, verbose_name="Proje İsmi")
    employees = models.ManyToManyField(Employee,verbose_name = "Çalışacaklar")
    efforts = models.DurationField(verbose_name = "Projenin Süresi")
    projectStatus = models.CharField(max_length=7, choices=status, default=1,verbose_name = "Proje Durumu")
    dead_line = models.DateField(verbose_name = "Projenin Bitiş Tarihi")
    company = models.ForeignKey(Company, on_delete=models.CASCADE,verbose_name = "Proje Sahibi Şirket")
    projectPoint = models.IntegerField(default=1, verbose_name="Proje Puanı")
    complete_per = models.FloatField(max_length=2, validators=[
                                     MinValueValidator(0), MaxValueValidator(100)],verbose_name = "Tamamlanma Performansı (100 üzerinden)")
    description = models.TextField(blank=True,verbose_name = "Proje Açıklaması")

    created_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now_add=False, auto_now=True)
    
    class Meta:
        ordering = ['projectName']

    def __str__(self):
        return (self.projectName)


class ProjectDetail(models.Model):

    projectName = models.ForeignKey(
        Projects, on_delete=models.CASCADE, verbose_name="Proje İsmi")
    projectEmployee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, verbose_name="Proje Çalışanı")

    def __str__(self):
        return str(self.projectName)


class Tasks(models.Model):

    tasksManager = models.ForeignKey(ProjectManager, on_delete = models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    employees = models.ManyToManyField(Employee)
    task_name = models.CharField(max_length=80)
    status = models.CharField(max_length=7, choices=status, default=1)
    due = models.CharField(max_length=7, choices=due, default=1)

    created_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now_add=False, auto_now=True)
    class Meta:
        ordering = ['project', 'task_name']

    def __str__(self):
        return(self.task_name)


class ManagerEmployees(models.Model):

    managers = models.ForeignKey(
        ProjectManager, verbose_name="Yönetici", on_delete=models.CASCADE)
    employee = models.ForeignKey(
        Employee, verbose_name="Çalışan", on_delete=models.CASCADE)
