from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm
import datetime
from django.contrib.auth.models import User


def profile(request, id):
    ctx = {}

    ctx['user'] = User.objects.get(id=id)
    
    return render(request, 'profile.html', ctx)
