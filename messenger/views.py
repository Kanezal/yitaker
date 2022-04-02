from messenger.models import Message, Chat
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from .forms import *
from django.urls import reverse_lazy
import datetime

def messages(request): 
    has_errors = False

    if request.method == 'POST': 
        form = MessageForm(request.POST)
        if form.is_valid():
            new_message = Message(user_sender = request.user_sender, text = form.cleaned_data['text'], date_receipt = datetime.now())
            new_message.save()

        else:
            has_errors = True
    else:
        form = MessageForm()
       

    page = int(request.GET.get('page') if request.GET.get('page') != None else 1)

    all_messages = Message.objects.order_by('-date_receipt')[(page - 1) * 10:(page - 1) * 10 + 10]
   # all_messages = Message.objects.order_by('-date_receipt')

    ctx = {
        'messages' : all_messages,
        'form' : form,
        'has_errors': has_errors
        }

    return render(request, 'messages.html', context = ctx)

def chats(request):
    has_errors = False

    if request.method == 'POST': 
        form = ChatForm(request.POST)
        if form.is_valid():
            chat_el = Chat(title = request.title, date_of_creation = datetime.now())
            chat_el.save()

        else:
            has_errors = True
    else:
        form = ChatForm()

    page = int(request.GET.get('page') if request.GET.get('page') != None else 1)
    all_chats = Message.objects.order_by('-date_receipt')[(page - 1) * 10:(page - 1) * 10 + 10]
    
    ctx = {
        'messages' : all_chats,
        'form' : form,
        'has_errors': has_errors
        }

    return render(request, 'chat.html', context = ctx)


    