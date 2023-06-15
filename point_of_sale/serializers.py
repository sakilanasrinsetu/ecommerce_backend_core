from rest_framework import serializers
from point_of_sale.models import POSUserAreas, POSUserRegions, POSProductInfo

class POSUserAreasSerializer(serializers.ModelSerializer):

    class Meta:
        model = POSUserAreas
        fields = '__all__'

class POSUserRegionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = POSUserRegions
        fields = '__all__'
        
class POSProductInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = POSProductInfo
        fields = '__all__'