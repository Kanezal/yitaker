from .models import ChatUser, Message, Chat
from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views.generic import CreateView
from .forms import *
from django.urls import reverse_lazy
import datetime


def messages(request, id): 
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
       
    
    try:
        all_messages = Message.objects.filter(chat_id=id).order_by('-date_receipt')
        chats_user = ChatUser.objects.filter(chat_id=Chat.objects.get(id=id))
        for chat_user in chats_user:
            if request.user == chat_user.user_id:
                ctx = {
                    'messages' : all_messages,
                    'form' : form,
                    'has_errors': has_errors
                }

                return render(request, 'messages.html', context = ctx)
    except Exception:
        pass
    
    raise Http404

def chats(request):
    has_errors = False

    if request.method == 'POST': 
        form = ChatForm(request.POST)
        if form.is_valid():
            chat_el = Chat(
            title = form.cleaned_data['title'],
            user_creator = request.user,
            date_of_creation = datetime.datetime.now(),
            )
            chat_el.save()

        else:
            has_errors = True
    else:
        form = ChatForm()

    all_chats =Chat.objects.all().order_by('-date_of_creation')


    ctx = {
        'chats' : all_chats,
        'form' : form,
        'has_errors': has_errors
    }

    return render(request, 'chats.html', context = ctx)
         