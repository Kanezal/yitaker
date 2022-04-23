from django.urls import path, re_path

from .views import *

urlpatterns = [
    # path('', имя_функции, name='имя_для_вызова'),
    path('chats/chat/<int:id>', messages),
    path('chats', chats),
    path('chats/delete<int:id>', delete)
]

# Имя для вызова это сокращенное название функции, то есть должен отражаться
# основной смысл view-функции.
