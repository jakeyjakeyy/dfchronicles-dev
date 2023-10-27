from rest_framework import serializers
from ..models import EntityPopulations
from .entity import EntitiesSerializer

class EntityPopulationsSerializer(serializers.ModelSerializer):
    entity = EntitiesSerializer(source='civ_id', read_only=True)
    class Meta:
        model = EntityPopulations
        fields = ['entity', 'race', 'population']