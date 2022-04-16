from django.shortcuts import render
from django.shortcuts import redirect

import datetime

from django.contrib import messages

from .forms import AddNoveltyForm

from news.models import Novelty
from news.models import NoveltyLikes


def new(request):
    all_news = Novelty.objects.all().order_by("-datetime")
    ctx = {
        'news': all_news,
    }
    return render(request, 'news.html', context=ctx)


def view_new_page(request, id):
    new = Novelty.objects.get(id=id)
    ctx = {
        'new': new,
    }
    return render(request, 'view_new_page.html', context=ctx)



def create_new_novelty(request):
    context = {}

    if request.method == 'POST':
        addform = AddNoveltyForm(request.POST, request.FILES)

        if addform.is_valid():
            if request.user.is_authenticated:
                record = Novelty(
                    name_new=addform.data['name_new'],
                    text=addform.data['text'],
                    sender=request.user,
                    picture=request.FILES['picture'],
                    datetime=datetime.datetime.now(),
                )
            else:
                record = Novelty(
                    name_new=addform.data['name_new'],
                    text=addform.data['text'],
                    picture=request.FILES['picture'],
                    datetime=datetime.datetime.now(),
                )
            record.save()
            id = record.id
            messages.add_message(request, messages.SUCCESS, "Пост успешно создан")
            return redirect('view_new_page', id=id)
        else:
            messages.add_message(request, messages.ERROR, "Некорректные данные")
            return redirect('create_new_novelty')
    else:
        if request.user.is_authenticated:
            context['addform'] = AddNoveltyForm(
                initial={
                    'sender': request.user,
                }
            )
        else:
            context['addform'] = AddNoveltyForm(
                initial={
                    'sender': 'Аноним',
                }
            )
    return render(request, 'create_new_novelty.html', context)


def create_new_novelty(request):
    context = {}

    if request.method == 'POST':
        addform = AddNoveltyForm(request.POST, request.FILES)

        if addform.is_valid():
            if request.user.is_authenticated:
                record = Novelty(
                    name_new=addform.data['name_new'],
                    text=addform.data['text'],
                    sender=request.user,
                    picture=request.FILES['picture'],
                    datetime=datetime.datetime.now(),
                )
            else:
                record = Novelty(
                    name_new=addform.data['name_new'],
                    text=addform.data['text'],
                    picture=request.FILES['picture'],
                    datetime=datetime.datetime.now(),
                )
            record.save()
            id = record.id
            messages.add_message(request, messages.SUCCESS, "Пост успешно создан")
            return redirect('view_new_page', id=id)
        else:
            messages.add_message(request, messages.ERROR, "Некорректные данные")
            return redirect('create_new_novelty')
    else:
        if request.user.is_authenticated:
            context['addform'] = AddNoveltyForm(
                initial={
                    'sender': request.user,
                }
            )
        else:
            context['addform'] = AddNoveltyForm(
                initial={
                    'sender': 'Аноним',
                }
            )
    return render(request, 'create_new_novelty.html', context)

