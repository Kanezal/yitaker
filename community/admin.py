from django.contrib import admin

from .models import ExistenceInGroup
from .models import Community

admin.site.register(ExistenceInGroup)
admin.site.register(Community)
