from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.


@login_required(login_url='/accounts/login')
def show_dashboard(request):
    return render(request, "dashboard/dashboard.html")


@login_required(login_url='/accounts/login')
def show_profile(request):
    return render(request, "dashboard/profile.html")
