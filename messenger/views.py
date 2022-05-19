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
            "Создать групповой чат": {
                "link": "create_chat"
            },
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
def chats(request):
    ctx = base_ctx()
    has_errors = False

    # if request.method == 'POST': 
    #     form = ChatForm(request.POST)
    #     if form.is_valid():
    #         chat_el = Chat(
    #         title = form.cleaned_data['title'],
    #         user_creator = request.user,
    #         date_of_creation = datetime.datetime.now(),
    #         )
    #         chat_el.save() 
    #     else:
    #         has_errors = True
    # else:
    #     form = ChatForm(id = request.user.id)
    
    chats_users = ChatUser.objects.filter(user_id = request.user)
    all_chat_list = []
    for chat_user in chats_users:
        chat = chat_user.chat_id
        chat.icon = ChatUser.objects.filter(~Q(user_id=request.user), Q(chat_id=chat))[0].user_id.profile.img
        all_chat_list.append(chat)
    ctx['chats'] = all_chat_list
    ctx['has_errors'] = has_errors

    return render(request, 'chats.html', context = ctx)

@login_required
def delete(request, id):
    if request.user == Message.objects.get(id=id).user_sender:
        message = Message.objects.get(id=id)
        message.isVisible_all_users = False
        message.save()
        return redirect(f"chat/{message.chat_id.id}") 
    return HttpResponse("<h1>ну это бан</h1>")

@login_required
def create(request):
    
    has_errors = False

    if request.method == 'POST': 
        form = ChatForm(request.POST, id = request.user.id)

        if form.is_valid():
            new_chat = GroupChat(
                title = form.cleaned_data['title'],
                user_creator = request.user,
                icon = form.cleaned_data['icon'],
                date_of_creation = datetime.datetime.now(),
            )
            new_chat.save()

            all_users = form.cleaned_data["option"]
            all_users.append(request.user.id)

            for user_id in all_users:
                chat_user = ChatUser(
                    chat_id = Chat.objects.get(id=new_chat.id),
                    user_id = User.objects.get(id=user_id),
                )
                chat_user.save()

            return redirect('chats')

        else:
            has_errors = True
    else:
        form = ChatForm(id = request.user.id)

    ctx = {
        'has_errors' : has_errors,
        'form' : form,
    }

    return render(request, 'create.html', context = ctx)