from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import MessageBoard


class MessageBoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MessageBoard
        fields = "__all__"
