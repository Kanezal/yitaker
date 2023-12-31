"""social_network URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from user_profile.urls import *
from search.urls import *
from news.urls import *
from messenger.urls import *
from community.urls import *
from friends.urls import *
from api.urls import *
from main.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('profile/', include('user_profile.urls')),
    path('search/', include('search.urls')),
    path('news/', include('news.urls')),
    path('search/', include('search.urls')),
    path('messenger/', include('messenger.urls')),
    path('community/', include('community.urls')),
    path('friends/', include('friends.urls')),
    path('registration/', include('registration.urls')),
    path('profile/', include('user_profile.urls')),
    path('api/', include('api.urls'))
]
