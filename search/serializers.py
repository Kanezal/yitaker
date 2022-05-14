from rest_framework import serializers
from django.contrib.auth.models import User
from news.models import Novelty
from community.models import Community

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name")

class NoveltySerializer(serializers.ModelSerializer):
    class Meta:
        model = Novelty
        fields = ("name_new",)

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ("name",)
