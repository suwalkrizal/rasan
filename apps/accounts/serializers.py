from rest_framework import serializers
from .models import User
from djoser.serializers import UserCreateSerializer, UserSerializer as DjoserUserSerializer

class CustomUserCreateSerializer(UserCreateSerializer):
    phone = serializers.CharField(required=False, allow_blank=True)
    address = serializers.CharField(required=False, allow_blank=True)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'username', 'password', 'email', 'phone', 'address')

class CustomUserSerializer(DjoserUserSerializer):
    phone = serializers.CharField(required=False, allow_blank=True)
    address = serializers.CharField(required=False, allow_blank=True)
    class Meta(DjoserUserSerializer.Meta):
        model = User
        fields = ('id', 'username', 'email', 'role', 'phone', 'address')