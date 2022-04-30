from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm
import datetime

def ProfileView(request):
    context = {}
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = Profile(
                city=form.cleaned_data['city'],
                other_socnet=form.cleaned_data['other_socnet'],
                career=form.cleaned_data['career'],
                interests=form.cleaned_data['interests'],
                favorite_musics=form.cleaned_data['favorite_musics'],
                favorite_movies=form.cleaned_data['favorite_movies'],
                favorite_TVshows=form.cleaned_data['favorite_TVshows'],
                favorite_books=form.cleaned_data['favorite_books'],
                favorite_games=form.cleaned_data['favorite_games'],
                favorite_quotes=form.cleaned_data['favorite_quotes'],
                status=form.cleaned_data['status'],
                about_me=form.cleaned_data['about_me'],
                life_position=form.cleaned_data['life_position'],
                political_preferences=form.cleaned_data['political_preferences'],
                world_outlook=form.cleaned_data['world_outlook'],
                main_in_life=form.cleaned_data['main_in_life'],
                main_in_people=form.cleaned_data['main_in_people'],
                attitude_to_smoking=form.cleaned_data['attitude_to_smoking'],
                attitude_to_alcohol=form.cleaned_data['attitude_to_alcohol'],
                inspires=form.cleaned_data['inspires'],
            )
            profile.save()
            return redirect('')
        else:
            context['form'] = form
    else:
        form = ProfileForm()
        context['form'] = form
    return render(request, 'profile.html', context)
