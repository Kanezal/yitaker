from django.urls import path, re_path
from django.contrib.auth import logout

from .views import *

urlpatterns = [
    # path('', имя_функции, name='имя_для_вызова'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_view, name='logout')
]

# Имя для вызова это сокращенное название функции, то есть должен отражаться
# основной смысл view-функции.
