from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', groups),
    path('<int:id>', view_group, name="view_group"),
    path('create/', create_new_group, name="create_new_group"),
    path('<int:id>/create', create_new_novelty)
]


