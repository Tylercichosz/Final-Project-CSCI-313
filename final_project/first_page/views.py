from django.shortcuts import render, get_object_or_404, redirect 
from .models import Course
from .forms import CourseForm
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def first_homePage(request):
    return render(request, 'index.html')
def about_basePage(request):
    return render(request, 'about_Us.html')
def profile_basePage(request):
    return render(request, 'profile.html')
def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

def course_list(request):
    courses = Course.objects.all()

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()

    context = {
        'courses': courses,
        'form': form
    }
    return render(request, 'course_list.html', context)

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    context = {'course': course}
    return render(request, 'course_detail.html', context)

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'create_course.html', {'form': form})

def course_add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            return redirect('http://127.0.0.1:8000/Courses/')
    else:
        form = CourseForm()
    return render(request, 'course_add.html', {'form': form})

def delete_course(request):
    course_id = request.POST.get('course_id')
    course = get_object_or_404(Course, id=course_id)
    course.delete()
    return JsonResponse({'status': 'success'})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('http://127.0.0.1:8000/Profile/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('http://127.0.0.1:8000/Profile/')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login credentials.'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/Profile/')



