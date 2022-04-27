from django.shortcuts import render
from .models import Community
from .forms import AddGroupForm
import datetime
from django.contrib import messages
from django.shortcuts import redirect
from news.forms import AddNoveltyForm
from news.models import Novelty
from .models import ExistenceInGroup

def base_ctx() -> dict:
    return {
        "nav": {
            "Создать сообщество": {
                "link": "/community/create/"
            },
            "Мои сообщества": {
                "link": "/community/my_communities/"
            },
            "Все сообщества": {
                "link": "/community/"
            }
        }
    }


def create_new_group(request):
    context = base_ctx()

    if request.method == 'POST':
        addform = AddGroupForm(request.POST, request.FILES)

        if addform.is_valid():
            if request.user.is_authenticated:
                record = Community(
                    name=addform.data['name'],
                    icon=addform.cleaned_data['icon'],
                    description=addform.data['description'],
                    creater=request.user,
                    datetime=datetime.datetime.now(),
                )
            record.save()
            id = record.id
            messages.add_message(request, messages.SUCCESS, "Группа успешно создана")
            return redirect('view_group', id=id)
        else:
            messages.add_message(request, messages.ERROR, "Некорректные данные")
            return redirect('create_new_group')
    else:
        if request.user.is_authenticated:
            context['addform'] = AddGroupForm(
                initial={
                    'creater': request.user,
                }
            )
    return render(request, 'create_new_group.html', context)


def view_group(request, id):
    ctx = base_ctx()

    group = Community.objects.get(id=id)
    news = Novelty.objects.all()

    e = ExistenceInGroup.objects.filter(user=request.user, group=Community.objects.get(id=id))
    existance = False

    if str(e) != "<QuerySet []>":
        existance = True

    ctx["group"] = group
    ctx["news"] = news
    ctx["existance"] = existance

    return render(request, 'view_group.html', context=ctx)


def groups(request):
    ctx = base_ctx()

    all_groups = Community.objects.all().order_by("-datetime")
    ctx['groups'] = all_groups

    return render(request, 'groups.html', context=ctx)


def create_new_novelty(request, id):
    context = {}

    group = Community.objects.get(id=id)

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
                    group=group,
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


def view_my_communities(request):
    all_communities = ExistenceInGroup.objects.all()
    my_communities = []
    for community in all_communities:
        if community.user == request.user:
            my_communities.append(community.group)

    ctx = {
        'groups': my_communities,
    }

    return render(request, 'view_my_communities.html', ctx)


def add_to_group(request, id):
    n = ExistenceInGroup(user=request.user, group=Community.objects.get(id=id))
    n.save()

    return redirect('view_group', id=id)


def delete_from_group(request, id):
    e = ExistenceInGroup.objects.filter(user=request.user, group=Community.objects.get(id=id)).delete()

    return redirect('view_group', id=id)