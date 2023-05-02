from django.shortcuts import render, get_object_or_404, redirect 
from .models import Course
from .forms import CourseForm


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
            return redirect('course_detail', course_id=course.id)
    else:
        form = CourseForm()
    return render(request, 'course_add.html', {'form': form})
