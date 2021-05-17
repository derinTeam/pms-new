from django import forms
from .models import ProjectManager
from .models import Company


class ManagerForms(forms.ModelForm):
    class Meta:
        model = ProjectManager
        fields = ["managerFirstName", "managerLastName",
                  "managerEmail", "managerPassword","username"]


class ManagerRegisterForms(forms.Form):

    #companyList = Company.objects.values_list('id', 'social_name')
    company = forms.ModelChoiceField(queryset=Company.objects.all(), initial=0)
    managerFirstName = forms.CharField(
         max_length=50, label="Yönetici İsim ")
    managerLastName = forms.CharField(max_length = 50,label = "Yönetici Soyisim ")
    username = forms.CharField(max_length = 50,label = "Kullanıcı Adı")
    managerEmail =  forms.EmailField(max_length = 254,label = "Yönetici Email")
    managerPassword = forms.CharField(max_length = 25,label = "Yönetici Parola", widget=forms.PasswordInput)
    
    confirm = forms.CharField(
        max_length=45, label="Parola Doğrulama", widget=forms.PasswordInput)


    def clean(self):
        company = self.cleaned_data.get("company")
        username = self.cleaned_data.get("username")
        managerFirstName = self.cleaned_data.get("managerFirstName")
        managerLastName = self.cleaned_data.get("managerLastName")
        managerEmail = self.cleaned_data.get("managerEmail")
        managerPassword = self.cleaned_data.get("managerPassword")
        confirm = self.cleaned_data.get("confirm")

        if managerPassword and confirm and managerPassword != confirm:
            raise forms.ValidationError("Parolalar Eşleşmiyor")

        values = {
            "company" : company,
            "username" : username,
            "managerFirstName": managerFirstName,
            "managerLastName": managerLastName,
            "managerEmail": managerEmail,
            "managerPassword": managerPassword
        }

        return values

class LoginForm(forms.Form):
    username = forms.EmailField(max_length = 50,label = "Email Adresi")
    password = forms.CharField(max_length = 20,label = "Parola", widget = forms.PasswordInput)

