from dataclasses import field
from rest_framework import serializers
#from .models import UserX
from django.contrib.auth.models import User

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        # Validate if user exists
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid credentials.')

        # Check password
        if not user.check_password(password):
            raise serializers.ValidationError('Invalid credentials or password.')

        attrs['user'] = user
        return attrs


