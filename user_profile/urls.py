from django.urls import path, re_path

from django.conf import settings
from django.conf.urls.static import static
from django.db.models import Q

from .views import *

urlpatterns = [
    path('<int:id>/', profile, name="profile"),
    path('settings/', profile_edit, name="profile_edit"),
    path('start_chat/<int:id>/', profile_start_chat, name="profile_start_chat"),
]

# Имя для вызова это сокращенное название функции, то есть должен отражаться
# основной смысл view-функции.
