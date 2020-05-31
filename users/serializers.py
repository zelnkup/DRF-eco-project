from djoser.serializers import UserSerializer
from rest_framework import serializers

from .models import MyCustomUser


class UserSerializer(UserSerializer):
	class Meta:
		model = MyCustomUser
		fields = ['email','id', 'username', 'points']


class CurrentUserSerializer(serializers.ModelSerializer):
    """The custom serializer which is the end point fot auth/me"""

    class Meta:
        model = MyCustomUser
        fields = ['id', 'code', 'points', 'email', 'username']