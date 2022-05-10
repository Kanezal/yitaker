from django.urls import path, re_path

from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', new),
    path('<int:id>', view_new_page, name="view_new_page"),
    path('<int:id>/add', add_like),
    path('<int:id>/delete', delete_like),
    path('from_friends/', news_from_friends),
    path('from_communities/', news_from_communities),
    path('from_communities&friends/', news_from_communities_friends),
]