from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')
@login_required(login_url='login')
def noaccesspg(request):
    return render(request, 'noaccess.html')

@login_required(login_url='login')  
def HomePage(request):
    return render(request, 'home.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'index.html')

def user_logout(request):  # Renamed to avoid conflict with Django's built-in logout
    logout(request)
    return redirect('index')
