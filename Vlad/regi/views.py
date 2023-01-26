from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm, RegForm

my_file = open("Base.txt", "r")
base = my_file.read()
lst = base.split()

def sign(request):
    if request.method == "POST":
        login = request.POST.get("Логин")
        password = request.POST.get("Пароль")
        user_check = login + password
        if user_check in lst:                              
            return render(request, "glavnaya.html")
        else:
            return HttpResponse(f"<h2>Неверный логин или пароль</h2>")
    else:
        userform = UserForm()
        return render(request, "sign.html", {"form": userform})

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
        return render(request, "register.html", {"form": userform})

def glavnaya(request):
    return render(request, "glavnaya.html")

def strim(request):
    return render(request, "Strim.html")

def gif(request):
    return render(request, "gif.html")

def video(request):
    return render(request, "video.html")

def strim1(request):
    return render(request, "strim1.html")

def strim2(request):
    return render(request, "strim2.html")

def strim3(request):
    return render(request, "strim3.html")

def strim4(request):
    return render(request, "strim4.html")

def strim5(request):
    return render(request, "strim5.html")

def strim6(request):
    return render(request, "strim6.html")

def video1(request):
    return render(request, "video1.html")

def video2(request):
    return render(request, "video2.html")

def video3(request):
    return render(request, "video3.html")

def video4(request):
    return render(request, "video4.html")

def video5(request):
    return render(request, "video5.html")

def video6(request):
    return render(request, "video6.html")






