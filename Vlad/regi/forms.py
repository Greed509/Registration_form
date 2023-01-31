from django import forms
 
class UserForm(forms.Form):
    login = forms.CharField(label="Логин", min_length=4, max_length=20)
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль",
    min_length=5, max_length=20)  
    required_css_class = "inputbox"
