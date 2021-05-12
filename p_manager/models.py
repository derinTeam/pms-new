from django.db import models
from django.contrib.auth.models import User
from employee.models import Employee
# Create your models here.
class Company(models.Model):
    social_name = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    city = models.CharField(max_length=50)
    found_date = models.DateField()

    class Meta:
        verbose_name_plural = 'Companies'
        ordering = ('name',)


    def __str__(self):
        return (self.name)

class ProjectManager(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    managerEmployees = models.ManyToManyField(Employee, blank=True)
    username = models.CharField(max_length = 50,verbose_name = "Kullanıcı Adı")
    managerFirstName = models.CharField(max_length = 50,verbose_name = "Yönetici İsim ")
    managerLastName = models.CharField(max_length = 50,verbose_name = "Yönetici Soyisim ")
    managerEmail =  models.EmailField(max_length = 254,verbose_name = "Yönetici Email")
    managerPassword = models.CharField(max_length = 25,verbose_name = "Yönetici Parola")
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
   
    def __str__(self):
        return (str(self.user))

    def invite(self, invite_profile):
        invite = Invite(inviter=self, invited=invite_profile)
        invites = invite_profile.received_invites.filter(inviter_id=self.id)
        if not len(invites) > 0:    # don't accept duplicated invites
            invite.save()

    def remove_employee(self, profile_id):
        employee = ProjectManager.objects.filter(id=profile_id)[0]
        self.managerEmployees.remove(employee)

class Invite(models.Model):
    inviter = models.ForeignKey(ProjectManager, on_delete=models.CASCADE, related_name='made_invites')
    invited = models.ForeignKey(ProjectManager, on_delete=models.CASCADE, related_name='received_invites')

    def accept(self):
        self.invited.managerEmployees.add(self.inviter)
        self.inviter.managerEmployees.add(self.invited)
        self.delete()

    def __str__(self):
        return str(self.inviter)