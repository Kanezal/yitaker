from django.urls import path, re_path

from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('my_friends/', my_friends, name="my_friends"),
    path('', friends, name="friends"),
    path('applications/', applications, name="applications"),
    path('is_friend/<int:id>', IsFriend.as_view()),
    path('add_friend/<int:id>', AddFriend.as_view()),
    path('accept_friend/<int:id>', AcceptFriend.as_view()),
    path('delete_friend/<int:id>', DeleteFriend.as_view()),
]
