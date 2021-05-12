from django import forms
from .models import Employee
from p_manager.models import ProjectManager


class EmployeeForms(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["employeeFirstName", "employeeLastName",
                  "employeeEmail"]


class EmployeeRegisterForm(forms.Form):

    
    employeeManager = forms.ModelChoiceField(queryset=ProjectManager.objects.all(), initial=0)
    employeeFirstName = forms.CharField(max_length=50, label="İsim")
    employeeLastName = forms.CharField(max_length=50, label="Soyisim")
    username = forms.CharField(max_length=50, label="Kullanıcı Adı")
    employeeEmail = forms.EmailField(max_length=124, label="Email")
    employeePassword = forms.CharField(
        max_length=45, label="Parola", widget=forms.PasswordInput)
    confirm = forms.CharField(
        max_length=45, label="Parola Doğrulama", widget=forms.PasswordInput)

    def clean(self):
        employeeManager = self.cleaned_data.get("employeeManager")
        username = self.cleaned_data.get("username")
        employeeFirstName = self.cleaned_data.get("employeeFirstName")
        employeeLastName = self.cleaned_data.get("employeeLastName")
        employeeEmail = self.cleaned_data.get("employeeEmail")
        employeePassword = self.cleaned_data.get("employeePassword")
        confirm = self.cleaned_data.get("confirm")
        if employeePassword and confirm and employeePassword != confirm:
            raise forms.ValidationError("Parolalar Eşleşmiyor")

        values = {
            "employeeManager" :employeeManager,
            "username" : username,
            "employeeFirstName": employeeFirstName,
            "employeeLastName": employeeLastName,
            "employeeEmail": employeeEmail,
            "employeePassword": employeePassword
        }

        return values
