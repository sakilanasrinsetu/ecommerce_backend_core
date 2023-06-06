# from base.serializers import BaseModelSerializer
from blogs.models import Blog
from rest_framework import serializers
from base.serializers import CreatedBySerializer,UpdatedBySerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class BlogSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(read_only=True)
    updated_by = serializers.CharField(read_only=True)
    slug = serializers.CharField(read_only=True)
    translation = serializers.JSONField(read_only=True)

    class Meta:
        model = Blog
        fields = "__all__"

    def to_representation(self, instance):
        self.fields["created_by"] = CreatedBySerializer(read_only=True)
        self.fields["updated_by"] = UpdatedBySerializer(read_only=True)

        return super(BlogSerializer, self).to_representation(instance)
    
    # def create(self,request, validated_data):
    #     blog_data = validated_data.pop('created_by', None)
    #     user = self
    #     self.create_or_update_student(user, student_data)
    #     return user
