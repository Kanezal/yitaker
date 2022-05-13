from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm
import datetime
from django.contrib.auth.models import User


def base_ctx(id, user) -> dict:
    ctx = {
        "nav": {
            "Профиль": {
                "link": "profile",
                "id": id,
            },
        }
    }
    if user == User.objects.get(id=id):
        ctx["nav"]["Настройки"] = {
            "link": "profile_edit",
        }
    return ctx

def profile(request, id):
    ctx = base_ctx(id, request.user)

    if id:
        ctx['user'] = User.objects.get(id=id)
    else:
        ctx['user'] = User.objects.get(id=request.user.id)

    return render(request, 'profile.html', ctx)


def profile_edit(request):
    ctx = base_ctx(request.user.id, request.user)

    profile = request.user.profile
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            profile = form.save()
    
    else:
        form = ProfileForm(instance=profile)
    
    ctx['form'] = form

    return render(request, 'profile_settings.html', ctx)

