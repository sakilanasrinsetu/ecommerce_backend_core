from django.contrib.auth import get_user_model
from rest_framework import serializers
User = get_user_model()


class CreatedBySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "password",
            "last_login",
            "date_joined",
            "groups",
            "user_permissions",
            "is_active",
        ]


class UpdatedBySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "password",
            "last_login",
            "date_joined",
            "groups",
            "user_permissions",
            "is_active",
        ]