from utils.base import *


class ProductSerializer(serializers.ModelSerializer):
    rating = serializers.FloatField(read_only = True)
    class Meta:
        model = Product
        fields = "__all__"