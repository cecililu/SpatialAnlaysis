from rest_framework import serializers
from .models import *

# class BuildingAttributeInformationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BuildingAttributeInformationModels
#         fields = ('house_metric_number', 'address', 'phone1', 'phone2', 'building')
        
                
class osmBuilding(serializers.ModelSerializer):
    class Meta:
        model = PlanetOsmPolygon
        fields ="__all__"