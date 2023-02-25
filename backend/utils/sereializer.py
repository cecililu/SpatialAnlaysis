from rest_framework import serializers
from .models import *

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = "__all__"
        
                
class osmBuilding(serializers.ModelSerializer):
    class Meta:
        model = PlanetOsmPolygon
        fields ="__all__"