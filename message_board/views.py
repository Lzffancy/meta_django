from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .models import MessageBoard
from .serializers import MessageBoardSerializer


class MessageBoardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MessageBoard.objects.all().order_by('-c_time')
    serializer_class = MessageBoardSerializer
    # permission_classes = [permissions.IsAuthenticated]  #权限控制
