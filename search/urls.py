from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', UsersListView.as_view(), ''),
]

