from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from .forms import ProfileUpdateForm


@login_required(login_url='/accounts/login')
def show_dashboard(request):
    return render(request, "dashboard/dashboard.html")


@login_required(login_url='/accounts/login')
def show_profile(request):
    profile_update_form = ProfileUpdateForm(request.POST or None, instance=request.user.profile)

    if profile_update_form.is_valid():
        profile_update_form.save()
        return redirect('profile')

    context = {
        'form': profile_update_form
    }

    return render(request, "dashboard/profile.html", context)
