from django.shortcuts import render

def first_homePage(request):
    return render(request, 'index.html')
def about_basePage(request):
    return render(request, 'about_Us.html')
def profile_basePage(request):
    return render(request, 'profile.html')
# Create your views here.
