from utils.base import *


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

    # def to_representation(self, instance):
    #     self.fields["selling_tax_category"] = TaxCategorySerializer()
    #     self.fields["buying_tax_category"] = TaxCategorySerializer()
    #     self.fields["brand"] = ProductBrandSerializer()
    #     #TODO
    #     # self.fields["pos_product_info"] = POSProductInfoS()
    #     self.fields["discount"] = DiscountSerializer()

    #     return super(ProductSerializer, self).to_representation(instance)
    
    def get_child(self, obj):
        if obj.status == "parent":
            qs = Product.objects.filter(parent_product = obj)
            serializer = ProductChildSerializer(qs, many = True)
            return serializer.data
        return None
    

class ProductListSerializer(serializers.ModelSerializer):
    parent_product_name = serializers.CharField(source='parent_product.name', read_only= True)
    rating = serializers.FloatField(read_only = True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'slug',
            'status',
            'parent_product_name',
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
            'discount',
        ]
