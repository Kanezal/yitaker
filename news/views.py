from django.shortcuts import render
from django.shortcuts import redirect

import datetime

from django.contrib import messages

from .forms import AddNoveltyForm

from news.models import Novelty
from news.models import NoveltyLikes


def view_new_page(request, id):
    new = Novelty.objects.get(id=id)
    ctx = {
        'new': new,
    }
    return render(request, 'view_new_page.html', context=ctx)



def new(request):
    context = {
        'news': Novelty.objects.all().order_by("-datetime")
    }

    if request.method == 'POST':
        addform = AddNoveltyForm(request.POST, request.FILES)

        if addform.is_valid():
            record = Novelty(
                name_new=addform.data['name_new'],
                text=addform.data['text'],
                sender=request.user if request.user.is_authenticated else None,
                picture=request.FILES['picture'],
                datetime=datetime.datetime.now(),
            )
            record.save()
            id = record.id
            messages.add_message(request, messages.SUCCESS, "Пост успешно создан")
        else:
            messages.add_message(request, messages.ERROR, "Некорректные данные")
    else:
        context['addform'] = AddNoveltyForm(
            initial={
                'sender': request.user if request.user.is_authenticated else "Аноним",
            }
        )
    
    return render(request, 'news.html', context)