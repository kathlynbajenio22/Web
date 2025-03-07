from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render

def home(request):
    return render(request, 'lms/home.html')

def login(request):
    return render(request, 'lms/login.html')

def logout(request):
    pass  # Implement logout logic

def user_registration(request):
    return render(request, 'lms/user_register.html')
