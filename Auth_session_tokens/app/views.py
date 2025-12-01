from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username , password=password)
        if user:
            login(request , user)
            return redirect("/dashboard/")
        else:
            return redirect(request , "login.html",{"error":"Invalid credentials"})
        
    return redirect(request , "login.html") 


def logout(request):
    logout(request)
    return redirect("/login/")

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        User.objects.create_user(username=username , password=password)
        return redirect("/login/")
    return redirect(request , "signup.html")

@login_required(login_url="/login/")
def dashboard(request):
    return redirect(request, "dashboard.html",{"user":request.user})