from audioop import add
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import redirect

import datetime

from django.contrib import messages

from community.models import ExistenceInGroup, Community
from friends.models import Friends
from .forms import AddNoveltyForm

from news.models import Novelty
from news.models import NoveltyLikes
from django.contrib.auth.decorators import login_required


def base_ctx() -> dict:
    return {
        "nav": {

            "Все новости": {
                "link": "news"
            },
            "Новости друзей&сообществ": {
                "link": "news_from_communities_friends"
            },
            "Новости друзей": {
                "link": "news_from_friends"
            },
            "Новости из сообществ": {
                "link": "news_from_communities"
            },
        }
    }


@login_required
def view_new_page(request, id):
    new = Novelty.objects.get(id=id)
    likes = len(NoveltyLikes.objects.filter(novelty=Novelty.objects.get(id=id)))
    l = NoveltyLikes.objects.filter(liked_by=request.user, novelty=Novelty.objects.get(id=id))
    is_liked = False

    if str(l) != "<QuerySet []>":
        is_liked = True
    ctx = {
        'new': new,
        'likes': likes,
        'is_liked': is_liked,
    }
    return render(request, 'view_new_page.html', context=ctx)


@login_required
def news(request):
    context = base_ctx()
    context['news'] = Novelty.objects.all().order_by("-datetime")
    if request.method == 'POST':
        addform = AddNoveltyForm(request.POST, request.FILES)

        if addform.is_valid():
            record = Novelty(
                name_new=addform.cleaned_data['name_new'],
                text=addform.cleaned_data['text'],
                sender=request.user,
                picture=addform.cleaned_data['picture'] if addform.cleaned_data['picture'] else None,
                datetime=datetime.datetime.now(),
            )
            record.save()
            messages.add_message(request, messages.SUCCESS, "Пост успешно создан")
            return redirect('news')
        else:
            messages.add_message(request, messages.ERROR, "Некорректные данные")
    else:
        context['form'] = AddNoveltyForm()

    return render(request, 'news.html', context)


@login_required
def news_from_friends(request):
    ctx = base_ctx()
    friends = list(Friends.objects.filter(user1=request.user, user2_confirmation=True)) + list(Friends.objects.filter(user2=request.user, user2_confirmation=True))
    n = list()
    for f in friends:
        if f.user1.id != request.user.id:
            id = f.user1.id
        else:
            id = f.user2.id
        n += Novelty.objects.filter(sender=User.objects.get(id=id))

    ctx["news"] = n
    ctx['len'] = len(n)

    return render(request, "filter_news.html", ctx)


@login_required
def news_from_communities(request):
    ctx = base_ctx()
    communities = ExistenceInGroup.objects.filter(user=request.user)
    n = list()
    for c in communities:
        id = c.group.id
        n += Novelty.objects.filter(group=Community.objects.get(id=id))

    ctx["news"] = n
    ctx['len'] = len(n)

    return render(request, "filter_news.html", ctx)


@login_required
def news_from_communities_friends(request):
    ctx = base_ctx()
    communities = ExistenceInGroup.objects.filter(user=request.user)
    friends = list(Friends.objects.filter(user1=request.user, user2_confirmation=True)) + list(
        Friends.objects.filter(user2=request.user, user2_confirmation=True))
    n = list()
    for f in friends:
        if f.user1.id != request.user.id:
            id = f.user1.id
        else:
            id = f.user2.id

        n += Novelty.objects.filter(sender=User.objects.get(id=id))

    for c in communities:
        id = c.group.id
        n += Novelty.objects.filter(group=Community.objects.get(id=id))

    n = list(set(n))

    ctx["news"] = n
    ctx['len'] = len(n)

    return render(request, "filter_news.html", ctx)


@login_required
def add_like(request, id):
    n = NoveltyLikes(liked_by=request.user, novelty=Novelty.objects.get(id=id))
    n.save()

    return redirect('view_new_page', id=id)


@login_required
def delete_like(request, id):
    n = NoveltyLikes.objects.filter(liked_by=request.user, novelty=Novelty.objects.get(id=id)).delete()

    return redirect('view_new_page', id=id)