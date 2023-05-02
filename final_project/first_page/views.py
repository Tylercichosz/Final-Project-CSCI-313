from django.shortcuts import render, get_object_or_404
from .models import Course



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
        
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'course_detail.html', {'course': course})
