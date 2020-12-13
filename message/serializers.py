from datetime import datetime

from django.contrib.auth.models import User
from rest_framework import serializers

from message.models import Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username',)


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer
    username = serializers.SerializerMethodField('getUsername')
    datum = serializers.DateTimeField(
        format='%d-%m-%Y %H:%M',
        default=datetime.now,
    )

    def getUsername(self, obj):
        return obj.sender.username

    class Meta:
        model = Message
        fields = ('sender', 'txt', 'datum', 'username',)
        read_only_fields = ('datum', 'username',)
