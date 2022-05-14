from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('user', SearchUserView, ''),
    path('novelty', SearchNoveltyView, ''),
    path('community', SearchCommunityView, ''),
    path('advanced', FilterView, ''),
]
