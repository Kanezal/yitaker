from django.shortcuts import render

from django.shortcuts import render
from .forms import ImageForm

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


def create_new_new(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            img_obj = form.instance
            return render(request, 'create_new_new.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'create_new_new.html', {'form': form})

