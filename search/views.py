from django.shortcuts import render
from django.contrib.auth import get_user_model
from .filters import *
from user_profile.models import Profile

def SearchView(request):
    # 1
    users = get_user_model().objects.all()
    user_filter = UserFilter(request.GET, queryset=users)
    users = user_filter.qs

    profiles = Profile.objects.all()
    profile_filter = ProfileFilter(request.GET, queryset=profiles)
    profiles = profile_filter.qs

    context = {'users' : users, 'UserFilter' : UserFilter, 'profiles' : profiles, 'ProfileFilter' : profile_filter}
    return render(request, 'search.html', context)
