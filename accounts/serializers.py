from rest_framework import serializers
from django.contrib.auth import authenticate
from . models import User


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

