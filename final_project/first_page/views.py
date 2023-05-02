from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .form import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required



def first_homePage(request):
    return render(request, 'index.html')
def about_basePage(request):
    return render(request, 'about_Us.html')
def profile_basePage(request):
    return render(request, 'profile.html')

def courses(request):
    courses = [
        {'title': 'Course 1', 'description': 'Description of Course 1'},
        {'title': 'Course 2', 'description': 'Description of Course 2'},
        {'title': 'Course 3', 'description': 'Description of Course 3'}


    ]
    return render(request,'courses.html', {'courses': courses})\
        
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = CustomAuthenticationForm()
    return render

def profile(request):
    return render(request, 'profile.html')