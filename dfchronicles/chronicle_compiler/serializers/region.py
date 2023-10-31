from rest_framework import serializers
from ..models import Regions

class RegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regions
        fields = ['name', 'type', 'id']
        
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regions
        fields = ['name', 'type', 'evilness', 'coords', 'force']