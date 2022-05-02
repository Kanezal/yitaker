from django.urls import path, re_path

from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('add_friend/<int:id>', AddFriend.as_view()),
    path('is_friend/<int:id>', IsFriend.as_view()),
]

# Имя для вызова это сокращенное название функции, то есть должен отражаться
# основной смысл view-функции.
