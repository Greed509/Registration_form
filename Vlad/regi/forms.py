from django import forms
 
class UserForm(forms.Form):
    Логин = forms.CharField()
    Пароль = forms.CharField()

class RegForm(forms.Form):
    Логин = forms.CharField()
    Пароль = forms.CharField()