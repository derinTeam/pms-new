from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 50,label = "Mail Adresi")
    password = forms.CharField(max_length = 20,label = "Parola", widget = forms.PasswordInput)

