from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from .models import Person
from django.core.exceptions import ObjectDoesNotExist

def sign(request):
    if request.method == "POST":
        login_input = request.POST.get("login")
        password_input = request.POST.get("password")
        user = Person.objects.in_bulk()
        for id in user:
            log_sql = (user[id].login)
            pas_sql = (user[id].password)
            if login_input == log_sql and password_input == pas_sql:           
                return render(request, "glavnaya.html") 
            else:
                return HttpResponse(f"<h2>Неверный логин или пароль</h2>")                    
    else:
        userform = UserForm()
        return render(request, "sign.html", {"form": userform})

def registration(request):
    if request.method == "POST":
        login_input = request.POST.get("login")
        password_input = request.POST.get("password")
        try:
            Person.objects.get(login=login_input)
            return HttpResponse(f"<h2>Пользователь {login_input} уже, существует!</h2>")
        except ObjectDoesNotExist:
            login_input = Person.objects.create(login=login_input, password=password_input)
            return HttpResponse(f"<h2>{login_input} успешно, зарегистрирован!</h2>")    
    else:
        userform = UserForm()        
        return render(request, "register.html", {"form": userform})