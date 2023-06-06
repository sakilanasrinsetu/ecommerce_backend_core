from blogs.models import Blog
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)