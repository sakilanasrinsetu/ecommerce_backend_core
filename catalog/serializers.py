# from base.serializers import BaseModelSerializer
from catalog.models import ProductGroup, Category, ProductBrand, TaxCategory
from rest_framework import serializers
from base.serializers import CreatedBySerializer,UpdatedBySerializer
from base.serializers import BaseModelSerializer
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

User = get_user_model()


class ProductGroupSerializer(BaseModelSerializer):

    class Meta:
        model = ProductGroup
        fields = "__all__"


class CategorySerializer(BaseModelSerializer):
    product_group = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=ProductGroup.objects.all()
    )
    child = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = Category
        fields = "__all__"

    def to_representation(self, instance):
        self.fields["product_group"] = ProductGroupSerializer()

        return super(CategorySerializer, self).to_representation(instance)

    def get_child(self, obj):
        if obj.status == "parent":
            qs = Category.objects.filter(category_parent = obj)
            serializer = CategorySerializer(qs, many = True)
            return serializer.data
        return None
    
class TaxCategorySerializer(BaseModelSerializer):

    class Meta:
        model = TaxCategory
        fields = "__all__"
    
class ProductBrandSerializer(BaseModelSerializer):

    class Meta:
        model = ProductBrand
        fields = "__all__"


class ProductCategoryVeryLiteSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'slug',
            'logo',
            'translation'
            ]


class ProductGroupWithCategoriesSerializer(ModelSerializer):
    categories = ProductCategoryVeryLiteSerializer(many=True, 
                                                    read_only=True)

    class Meta:
        model = ProductGroup
        fields = [
            "id",
            "name",
            "slug",
            "ordering",
            "categories",
            "translation",
        ]

