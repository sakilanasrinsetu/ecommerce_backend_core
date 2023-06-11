# from base.serializers import BaseModelSerializer
from blogs.models import Blog
from rest_framework import serializers
from base.serializers import CreatedBySerializer,UpdatedBySerializer, BaseModelSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class BlogSerializer(BaseModelSerializer):
    slug = serializers.CharField(read_only=True)
    translation = serializers.JSONField(read_only=True)

    class Meta:
        model = Blog
        fields = "__all__"
