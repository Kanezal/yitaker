from django.shortcuts import render

from news.models import Novelty


def new(request):
    all_news = Novelty.objects.all()
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




