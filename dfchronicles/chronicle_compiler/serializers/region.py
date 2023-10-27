from rest_framework import serializers
from ..models import Regions

class RegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regions
        fields = ['name', 'type']