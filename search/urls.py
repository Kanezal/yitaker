from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('user', SearchUserView, name='search_user'),
    path('novelty', SearchNoveltyView, name='search_novelty'),
    path('community', SearchCommunityView, name='search_community'),
    path('advanced', FilterView, name='search_advanced'),
]
