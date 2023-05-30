from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from pyexpat.errors import messages

from tasks.models import *


def index(request):
    return render(request, "index.html")
def signin(request):
    return render(request, "signin.html")
def prodjects(request):
    return render(request, "prodjects.html")
def login(request):
    return render(request, "login.html")
def test(request):
    obj = Users.objects.order_by("id_role")
    return render(request, "test.html", {"obj": obj})

def success(request):
    if request.method == "POST":
        log = request.POST['login']
        pas = request.POST['password']
        worker = authenticate(request, login=log, password=pas)
        if (worker is not None):
            login(request, worker)
            return redirect("/")
        else:
            messages.error(request, "Данные не верны, пожалуйста повторите вход")
            return redirect("prodject.html")

    else:
        return render(request, "login.html")