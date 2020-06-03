from djoser.serializers import UserSerializer
from rest_framework import serializers

from .models import MyCustomUser


class UserSerializer(UserSerializer):
	class Meta:
		model = MyCustomUser
		fields = ['email', 'id', 'username', 'current_points', 'all_points']


class CurrentUserSerializer(serializers.ModelSerializer):
	"""The custom serializer which is the end point fot auth/me"""

	class Meta:
		model = MyCustomUser
		fields = ['id', 'code', 'current_points', 'all_points', 'email', 'username']
