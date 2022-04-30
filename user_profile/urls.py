from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', ProfileView, name=''),
]

# Имя для вызова это сокращенное название функции, то есть должен отражаться
# основной смысл view-функции.
