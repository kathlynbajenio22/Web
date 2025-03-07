from django.shortcuts import render

def home(request):
    return render(request, "home.html")  # Make sure home.html exists in your templates folder

def user_registration(request):
    return render(request, "register.html")  

def user_login(request):
    return render(request, "user_login.html")# Make sure register.html exists in your templates folder