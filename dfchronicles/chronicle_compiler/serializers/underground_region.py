from rest_framework import serializers
from ..models import UndergroundRegions

class UndergroundRegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UndergroundRegions
        fields = ['type', 'depth']