from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('novelty', SearchNoveltyView, name='search_novelty'),
    path('community', SearchCommunityView, name='search_community'),
    path('', FilterView, name='search_advanced'),
]
