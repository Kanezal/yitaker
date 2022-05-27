from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm
import datetime
from django.contrib.auth.models import User
from messenger.models import Chat, ChatUser

from django.urls import reverse
from django.http import HttpResponse

from django.db.models import Q


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
    else:
        ctx["nav"]["Переписка"] = {
            "link": "profile_start_chat",
            "id": id,
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
    fields = [
            'city', 'other_socnet', 'career',
            'interests', 'favorite_musics',
            'favorite_movies', 'favorite_movies',
            'favorite_TVshows', 'favorite_books',
            'favorite_games', 'favorite_quotes',
            'status', 'about_me', 'life_position',
            'political_preferences', 'world_outlook',
            'world_outlook', 'main_in_life', 'main_in_people',
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


def profile_start_chat(request, id):
    if request.user.id == id:
        return redirect('/')
    
    chats = ChatUser.objects.filter(user_id=request.user)
    for chat in chats:
        chat = chat.chat_id
        another_chat = ChatUser.objects.filter(~Q(user_id=request.user), Q(chat_id=chat))
        if len(another_chat) > 0:
            return redirect(reverse('chat', args=(chat.id,)))
    
    new_chat = Chat(
        title=f"Чат между {request.user.first_name} и {User.objects.get(id=id).first_name}"
    )
    new_chat.save()
    ChatUser(
        chat_id = new_chat,
        user_id = request.user,
    ).save()
    ChatUser(
        chat_id = new_chat,
        user_id = User.objects.get(id=id),
    ).save()

    return redirect(reverse('chat', args=(new_chat.id, )))