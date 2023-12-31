from django.urls import path, re_path

from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', groups, name="all_groups"),
    path('<int:id>', view_group, name="view_group"),
    path('create/', create_new_group, name="create_new_group"),
    path('<int:id>/create', create_new_novelty, name="create_novelty"),
    path('<int:id>/add', add_to_group, name="add_to_group"),
    path('<int:id>/delete', delete_from_group, name="delete_from_group"),
    path('<int:id>/members/', members),
    path('my_communities/', view_my_communities, name="view_my_communities"),
]

