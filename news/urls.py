from django.urls import path, re_path

from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', new),
    path('<int:id>', view_new_page, name="view_new_page"),
]