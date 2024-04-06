from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm, LoginForm, FarmerForm, FarmerWeightForm
from django.contrib.auth.models import User
from farmers.models import Farmer



def dashboard(request):
    return render(request, 'registration/dashboard.html')

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin-dashboard')
        else:
            # Return form with errors
            return render(request, 'registration/login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})
        
def user_logout(request):
    logout(request)
    return redirect('login')

def admin_dashboard(request):
    if request.method == 'POST':
       form = FarmerWeightForm(request.POST)
       if form.is_valid():
           farmer = form.cleaned_data.get('Farmer')
           weight = form.cleaned_data.get('berry_weight')
           farmer.berry_weight = weight
           farmer.save()
           return redirect('admin-dashboard')
    else:
        form = FarmerWeightForm()
    return render(request, 'admin/admin_dashboard.html', {'form': form})

def register_new_farmer(request):
    if request.method == 'POST':
        form = FarmerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin-dashboard')
    else:
        form = FarmerForm()
    return render(request, 'admin/register_farmer.html', {'form': form})