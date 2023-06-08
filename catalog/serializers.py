# from base.serializers import BaseModelSerializer
from catalog.models import ProductGroup, Category, ProductBrand, TaxCategory
from rest_framework import serializers
from base.serializers import CreatedBySerializer,UpdatedBySerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class ProductGroupSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = ProductGroup
        fields = "__all__"

    def to_representation(self, instance):
        self.fields["created_by"] = CreatedBySerializer(read_only=True)
        self.fields["updated_by"] = UpdatedBySerializer(read_only=True)

        return super(ProductGroupSerializer, self).to_representation(instance)

class CategorySerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(read_only=True)
    updated_by = serializers.CharField(read_only=True)
    product_group = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=ProductGroup.objects.all()
    )
    child = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = Category
        fields = "__all__"

    def to_representation(self, instance):
        self.fields["created_by"] = CreatedBySerializer(read_only=True)
        self.fields["updated_by"] = UpdatedBySerializer(read_only=True)
        self.fields["product_group"] = ProductGroupSerializer()

        return super(CategorySerializer, self).to_representation(instance)

    def get_child(self, obj):
        a = 'gfb'
        if obj.status == "parent":
            qs = Category.objects.filter(category_parent = obj)
            serializer = CategorySerializer(qs, many = True)
            return serializer.data
        return None