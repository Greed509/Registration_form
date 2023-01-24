from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm, RegForm

my_file = open("Base.txt", "r")
base = my_file.read()
lst = base.split()

def index(request):
    if request.method == "POST":
        login = request.POST.get("Логин")
        password = request.POST.get("Пароль")
        user_check = login + password
        if user_check in lst:                              
            return HttpResponse(f"<h2>Привет, {login}</h2>")
                #Добавить переадресацию
        else:
            return HttpResponse(f"<h2>Неверный логин или пароль</h2>")
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})

def registration(request):
    if request.method == "POST":
        login = request.POST.get("Логин")
        password = request.POST.get("Пароль")
        user_check = login + password
        if user_check not in lst:        
            my_file = open("Base.txt", "a+")
            my_file.write(user_check)
            my_file.write(' ')
            my_file.close()
            return HttpResponse(f"<h2>{login} успешно, зарегистрирован!</h2>")
        else:
            return HttpResponse(f"<h2>Пользователь {login} уже, существует!</h2>")      
    else:
        userform = RegForm()        
        return render(request, "registration.html", {"form": userform})