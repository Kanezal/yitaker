from django.urls import path, re_path

from .views import *

urlpatterns = [
    # path('', имя_функции, name='имя_для_вызова'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
]

# Имя для вызова это сокращенное название функции, то есть должен отражаться
# основной смысл view-функции.
