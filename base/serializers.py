from django.contrib.auth import get_user_model
from rest_framework import serializers
from base.models import BaseModel
from rest_framework.serializers import SerializerMethodField, ModelSerializer
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

class BaseModelSerializer(ModelSerializer):
    created_by = serializers.CharField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = BaseModel
        abstract = True

    def to_representation(self, instance):
        self.fields["created_by"] = CreatedBySerializer(read_only=True)
        self.fields["updated_by"] = UpdatedBySerializer(read_only=True)

        return super(BaseModelSerializer, self).to_representation(instance)