from rest_framework import serializers
from ..models import HistoricalFigures

class HistoricalFiguresSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalFigures
        fields = ['name', 'race', 'birth_year']

class HistoricalFigureSerializer(serializers.ModelSerializer):
    # used_identity = IdentitySerializer(source='used_identity', read_only=True)
    # ent_pop = EntityPopulationSerializer(source='entity_population', read_only=True)
    # current_identity
    # held_artifacts
    class Meta:
        fields = ['appeared', 'associated_type', 'birth_year', 'caste', 'death_year', 'deity', 'goal', 'journey_pet', 'name', 'race', 'sphere', 'force', 'animated', 'animated_string', 'used_identity', 'entity_population', 'current_identity', 'held_artifacts']