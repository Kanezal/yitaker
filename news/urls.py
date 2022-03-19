from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', new),
    path('<int:id>', view_new_page),
]


