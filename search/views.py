from django.shortcuts import render
from django.contrib.auth import get_user_model
from user_profile.models import Profile
from news.models import Novelty
from community.models import Community
from .filters import ProfileFilter
from .serializers import *
from django.contrib.auth.decorators import login_required



@login_required
def SearchUserView(request):
    context = {}
    users = get_user_model().objects.all()
    serializer = UserSerializer(users, many=True)
    context['data'] = serializer.data
    return render(request, 'search_user.html', context)


@login_required
def SearchNoveltyView(request):
    context = {}
    novelties = Novelty.objects.all()
    serializer = NoveltySerializer(novelties, many=True)
    context['data'] = serializer.data
    return render(request, 'search_novelty.html', context)


@login_required
def SearchCommunityView(request):
    context = {}
    communities = Community.objects.all()
    serializer = CommunitySerializer(communities, many=True)
    context['data'] = serializer.data
    return render(request, 'search_community.html', context)


@login_required
def FilterView(request):
    context = {}
    profiles = Profile.objects.all()
    profile_filter = ProfileFilter(request.GET, queryset=profiles)
    profiles = profile_filter.qs
    context['profiles'] = profiles
    context['ProfileFilter'] = profile_filter
    return render(request, 'filter.html', context)
