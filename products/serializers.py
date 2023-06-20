from utils.base import *
from rest_framework import serializers
from point_of_sale.models import POSProductInfo


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'status',
        ]

class ProductChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'slug',
            'status',
        ]

class ProductSerializer(serializers.ModelSerializer):
    rating = serializers.FloatField(read_only = True)
    child = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = Product
        fields = "__all__"

    def to_representation(self, instance):
        self.fields["selling_tax_category"] = TaxCategorySerializer()
        self.fields["buying_tax_category"] = TaxCategorySerializer()
        self.fields["brand"] = ProductBrandSerializer()
        #TODO
        self.fields["categories"] = CategoryListSerializer(read_only=True, many=True)
        self.fields["sub_categories"] = CategoryListSerializer(read_only=True, many=True)
        self.fields["discount"] = DiscountSerializer()

        return super(ProductSerializer, self).to_representation(instance)
    
    def get_child(self, obj):
        if obj.status == "parent":
            qs = Product.objects.filter(parent_product = obj)
            serializer = ProductChildSerializer(qs, many = True)
            return serializer.data
        return None

class ProductListSerializer(serializers.ModelSerializer):
    parent_product = serializers.CharField(source='parent_product.name', read_only= True)
    categories = serializers.SerializerMethodField(read_only= True)
    sub_categories = serializers.SerializerMethodField(read_only= True)
    discount = serializers.CharField(source='discount.name', read_only= True)
    rating = serializers.FloatField(read_only = True)
    pos_product_info = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'slug',
            'categories',
            'sub_categories',
            'status',
            'parent_product',
            'metaTitle',
            'is_active',
            'is_featured',
            'brand',
            'images',
            'brand',
            'is_top_sale',
            'is_upcoming',
            'on_the_go',
            'is_special_day',
            'rating',
            'is_only_pos',
            'sku',
            'discount',
            'pos_product_info',
        ]

    def get_categories(self, obj):
        if obj.categories:
            serializer = CategoryListSerializer(
                obj.categories, many = True
            )
            return serializer.data
        return None
    
    def get_sub_categories(self, obj):
        if obj.sub_categories:
            serializer = CategoryListSerializer(
                obj.sub_categories, many = True
            )
            return serializer.data
        return None    
    
    def get_pos_product_info(self, obj):
        if obj.pos_product_info:
            serializer = POSProductInfoSerializer(
                obj.pos_product_info
            )
            return serializer.data
        return None


class POSProductInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = POSProductInfo
        fields = '__all__'


class POSProductCreateSerializer(serializers.ModelSerializer):
    pos_product_info = POSProductInfoSerializer()

    class Meta:
        model = Product
        fields = '__all__'