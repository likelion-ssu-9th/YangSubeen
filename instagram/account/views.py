from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = RegisterForm(request=request, data = request.POST)

        return redirect("home") 


def logout_view(request):
    logout(request)
    return redirect("home")

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        return render(request, 'signup.html', {'form': form })