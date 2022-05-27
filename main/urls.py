from django.urls import path, re_path

from django.conf import settings
from django.conf.urls.static import static
from django.db.models import Q

from .views import *

urlpatterns = [
    path('', main_page, name="main_page"),
    path('future_plans/', future_plans, name="future_plans"),
    path('command/', command, name="command")
]