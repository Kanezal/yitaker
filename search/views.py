from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer

from django.contrib.auth.models import User
from .serializers import UsersListSerializer
from django.contrib.auth import get_user_model

class UsersListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'search.html'

    def get(self, request):
        users = get_user_model().objects.all()
        serializer = UsersListSerializer(users, many=True)
        return Response({'data': serializer.data})

