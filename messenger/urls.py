from django.urls import path, re_path

from .views import *

urlpatterns = [
    # path('', имя_функции, name='имя_для_вызова'),
    path('messages/<int:id>', messages, name = 'messages'),
    path('chats', chats, name = 'chats')
]

# Имя для вызова это сокращенное название функции, то есть должен отражаться
# основной смысл view-функции.
