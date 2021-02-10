from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate

def home(request):
    context = {}

    return render(request, 'base.html', context)

def register_user(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')

            messages.success(request, f'Account created for '+ email)

            return redirect('login')
        else:
            messages.warning(request, 'Please enter valid fields')
    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'register.html', context)

def login_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)
        print("User:", user)
        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.warning(request, f'Please enter valid credentials!')

    context = {}

    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('Home')