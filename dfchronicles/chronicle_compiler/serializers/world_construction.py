from rest_framework import serializers
from ..models import WorldConstruction

class WorldConstructionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorldConstruction
        fields = ['name', 'type']