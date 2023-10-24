from rest_framework import serializers
from .models import World, Artifact

class WorldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = World
        fields = ['id', 'name', 'name2', 'owner']

class WorldSerializer(serializers.ModelSerializer):
    class Meta:
        model = World
        fields = ['id', 'name', 'name2', 'owner', 'world_artifacts', 'world_entities', 'world_entity_populations', 'world_occasion', 'world_historical_eras', 'world_historical_event_collections', 'world_historical_events', 'world_historical_figures', 'world_regions', 'world_sites', 'world_structures', 'world_underground_regions', 'world_written_contents', 'world_world_construction', 'world_musical_forms', 'world_poetic_forms', 'world_dance_forms', 'world_landmass', 'world_mountain_peak']

class ArtifactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artifact
        fields = ['name', 'name2', 'item_type'] 