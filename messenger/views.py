from genericpath import exists
from .models import ChatUser, Message, Chat, GroupChat
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
import datetime
from friends.models import Friends
from django.db.models import Q

from django.contrib.auth.decorators import login_required

def base_ctx() -> dict:
    return {
        "nav": {
        }
    }

@login_required
def messages(request, id): 
    ctx = base_ctx()

    has_errors = False

    if request.method == 'POST': 
        form = MessageForm(request.POST)
        if form.is_valid():
            new_message = Message(
                user_sender = request.user,
                text = form.cleaned_data['text'],
                date_receipt = datetime.datetime.now(),
                chat_id = Chat.objects.get(id=id)
            )
            new_message.save()
            return redirect('chat', id=id)
        else:
            has_errors = True
    else:
        form = MessageForm()
           
    all_messages = Message.objects.filter(
        chat_id=id,
        isVisible_all_users = True
    ).order_by('date_receipt')

    try:
        chats_user = ChatUser.objects.filter(chat_id=Chat.objects.get(id=id))
    except ObjectDoesNotExist:
        raise Http404

    for chat_user in chats_user:
        if request.user == chat_user.user_id:
            ctx['messages'] = all_messages
            ctx['form'] = form
            ctx['has_errors'] = has_errors
            ctx['title'] = Chat.objects.get(id=id).title
            
            return render(request, 'messages.html', context = ctx)


@login_required
def delete(request, id):
    if request.user == Message.objects.get(id=id).user_sender:
        message = Message.objects.get(id=id)
        message.isVisible_all_users = False
        message.save()
        return redirect(f"chat/{message.chat_id.id}") 
    return HttpResponse("<h1>ну это бан</h1>")

@login_required
def chats(request):
    ctx = base_ctx()
    has_errors = False

    chats_users = ChatUser.objects.filter(user_id = request.user)
    all_chat_list = []
    for chat_user in chats_users:
        chat = chat_user.chat_id
        
        user2 = ChatUser.objects.filter(
            ~Q(user_id=request.user), 
            Q(chat_id=chat)
        )[0].user_id

        chat.title = f"{user2.first_name} {user2.last_name}"
        chat.icon = user2.profile.img
        all_chat_list.append(chat)

    ctx['chats'] = all_chat_list
    ctx['has_errors'] = has_errors
    ctx['len'] = len(all_chat_list)

    return render(request, 'chats.html', context = ctx)

@login_required
def profile_start_chat(request, id):
    if request.user.id == id:
        return redirect('/')
    
    user_prof = User.objects.get(id=id)
    user_re = request.user

    if str(Chat.objects.filter(user1 = user_re, user2 = user_prof)) == "<QuerySet []>" and str(Chat.objects.filter(user1 = user_prof, user2 = user_re))  == "<QuerySet []>":
        new_chat = Chat(
            user1 = user_re,
            user2 = user_prof
            )
        new_chat.save()

        new_chatuser1 = ChatUser(
            chat_id = Chat.objects.get(id = new_chat.id),
            user_id = user_re
            )
        new_chatuser1.save()

        new_chatuser2 = ChatUser(
            chat_id = Chat.objects.get(id = new_chat.id),
            user_id = user_prof
            )
        new_chatuser2.save()

        return redirect('chat', id=new_chat.id)

    elif str(Chat.objects.filter(user1 = user_prof, user2 = user_re)) != "<QuerySet []>":
        return redirect('chat', id=Chat.objects.get(user1=user_prof, user2=user_re).id)

    else:
        return redirect('chat', id=Chat.objects.get(user1=user_re, user2=user_prof).id)