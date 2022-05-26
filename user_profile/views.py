from django.shortcuts import render, redirect

from news.models import Novelty
from .models import Profile
from .forms import ProfileForm
import datetime
from django.contrib.auth.models import User
from messenger.models import Chat, ChatUser

from django.urls import reverse
from django.http import HttpResponse

from django.db.models import Exists, OuterRef, Q
from django.contrib.auth.decorators import login_required

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
    #else:
    #    ctx["nav"]["Переписка"] = {
    #        "link": "profile_start_chat",
    #        "id": id,
    #    }
    return ctx


@login_required
def profile(request, id):
    ctx = base_ctx(id, request.user)

    if id:
        ctx['user'] = User.objects.get(id=id)
    else:
        ctx['user'] = User.objects.get(id=request.user.id)

    ctx['news'] = Novelty.objects.filter(sender=id).order_by("-datetime")

    return render(request, 'profile.html', ctx)


@login_required
def profile_edit(request):
    ctx = base_ctx(request.user.id, request.user)
    fields = [
            'city', 'other_socnet', 'career',
            'interests', 'favorite_musics',
            'favorite_movies', 'favorite_movies',
            'favorite_TVshows', 'favorite_books',
            'favorite_games', 'favorite_quotes',
            'status', 'about_me', 'life_position',
            'political_preferences', 'world_outlook',
            'world_outlook', 'main_in_life',
            'attitude_to_smoking', 'attitude_to_alcohol',
            'inspires',
        ]

    profile = request.user.profile
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            profile = form.save()
    
    else:
        form = ProfileForm(instance=profile)
    
    ctx['form'] = form
    profile.rating = 0
    for field in fields:
        if getattr(profile, field) != None:
            profile.rating += len(getattr(profile, field))//10
    if profile.img_confirmation:
        profile.rating += 20
    profile.save()



    return render(request, 'profile_settings.html', ctx)

