from django.shortcuts import render
from django.contrib.auth import get_user_model
from user_profile.models import Profile
from news.models import Novelty
from community.models import Community
from .filters import ProfileFilter
from .serializers import *


def base_ctx() -> dict:
    return {
        "nav": {
            "Поиск пользователя по интересам": {
                "link": "search_advanced"
            },
            # "Поиск новостей": {
            #     "link": "search_novelty"
            # },
            # "Поиск сообществ": {
            #     "link": "search_community"
            # },
        }
    }


def SearchUserView(request):
    context = base_ctx()
    users = get_user_model().objects.all()
    serializer = UserSerializer(users, many=True)
    context['data'] = serializer.data
    return render(request, 'search_user.html', context)

def SearchNoveltyView(request):
    context = base_ctx()
    novelties = Novelty.objects.all()
    serializer = NoveltySerializer(novelties, many=True)
    context['data'] = serializer.data
    return render(request, 'search_novelty.html', context)

def SearchCommunityView(request):
    context = base_ctx()
    communities = Community.objects.all()
    serializer = CommunitySerializer(communities, many=True)
    context['data'] = serializer.data
    return render(request, 'search_community.html', context)

def FilterView(request):
    context = base_ctx()
    profiles = Profile.objects.all()
    profile_filter = ProfileFilter(request.GET, queryset=profiles)
    profiles = profile_filter.qs
    context['profiles'] = profiles
    context['ProfileFilter'] = profile_filter
    return render(request, 'filter.html', context)