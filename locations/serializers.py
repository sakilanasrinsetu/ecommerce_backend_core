from rest_framework import serializers
from .models import  Division, District, Area, StoreLocation


class DivisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Division
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    division_details = serializers.SerializerMethodField(read_only = True)


    class Meta:
        model = Division
        fields = '__all__'

    def get_division_details(self, obj):
        if obj.division:
            serializer = DivisionSerializer(instance=obj.division)
            return serializer.data
        return None


class AreaSerializer(serializers.ModelSerializer):
    district_details = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = Area
        fields = '__all__'


    def get_district_details(self, obj):
        if obj.district:
            serializer = DistrictSerializer(instance=obj.district)
            return serializer.data
        return None


class StoreLocationSerializer(serializers.ModelSerializer):
    area_details = serializers.SerializerMethodField(read_only = True)


    class Meta:
        model = StoreLocation
        fields = '__all__'

    def get_area_details(self, obj):
        if obj.area:
            serializer = AreaSerializer(instance=obj.area)
            return serializer.data
        return None