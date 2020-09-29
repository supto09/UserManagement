from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import LoginForm, RegisterWithProfile


def show_login(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        user = authenticate(email=email, password=password)
        login(request, user)
        return redirect('dashboard')

    context = {
        'form': form
    }

    return render(request, "accounts/login.html", context)


def show_register(request):
    form = RegisterWithProfile(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')

    context = {
        'form': form
    }

    return render(request, 'accounts/register.html', context)


def show_logout(request):
    logout(request)
    return redirect('dashboard')
