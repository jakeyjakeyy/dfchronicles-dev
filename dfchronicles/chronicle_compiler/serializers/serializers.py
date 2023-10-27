# from rest_framework import serializers
# from .models import World, Artifact, Entities, EntityPopulations, Occasion, HistoricalEras, HistoricalEventCollections, HistoricalEvents, HistoricalFigures, Regions, Sites, Structures, UndergroundRegions, WrittenContents, WorldConstruction, IntriguePlot, Landmass, MountainPeak, Identities

# class WorldsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = World
#         fields = ['id', 'name', 'name2', 'owner']

# class WorldSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = World
#         fields = ['id', 'name', 'name2', 'owner', 'world_artifacts', 'world_entities', 'world_entity_populations', 'world_occasion', 'world_historical_eras', 'world_historical_event_collections', 'world_historical_events', 'world_historical_figures', 'world_regions', 'world_sites', 'world_structures', 'world_underground_regions', 'world_written_contents', 'world_world_construction', 'world_musical_forms', 'world_poetic_forms', 'world_dance_forms', 'world_landmass', 'world_mountain_peak']

# class HistoricalFiguresSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HistoricalFigures
#         fields = ['name', 'race', 'birth_year']

# class HistoricalFigureSerializer(serializers.ModelSerializer):
#     # used_identity = IdentitySerializer(source='used_identity', read_only=True)
#     # ent_pop = EntityPopulationSerializer(source='entity_population', read_only=True)
#     # current_identity
#     # held_artifacts
#     class Meta:
#         fields = ['appeared', 'associated_type', 'birth_year', 'caste', 'death_year', 'deity', 'goal', 'journey_pet', 'name', 'race', 'sphere', 'force', 'animated', 'animated_string', 'used_identity', 'entity_population', 'current_identity', 'held_artifacts']

# class SitesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sites
#         fields = ['name', 'type']

# class StructuresSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Structures
#         fields = ['name', 'type']
        
# class WrittenContentsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = WrittenContents
#         fields = ['title', 'form']
        
# class HistoricalEventsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HistoricalEvents
#         fields = ['type']

# class ArtifactsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Artifact
#         fields = ['name', 'name2', 'item_type', 'id'] 
# class ArtifactSerializer(serializers.ModelSerializer):
#     site = SitesSerializer(source='site_id', read_only=True)
#     holder = HistoricalFiguresSerializer(source='holder_id', read_only=True)
#     wc = WrittenContentsSerializer(source='written_content_id', read_only=True)
#     structure = StructuresSerializer(source='structure_id', read_only=True)
#     events = HistoricalEventsSerializer(source='artifact_historical_events', many=True, read_only=True)
#     class Meta:
#         model = Artifact
#         fields = ['name', 'name2', 'site', 'holder', 'page_number', 'wc', 'item_type', 'material', 'item_subtype', 'item_description', 'structure', 'events', 'artifact_intrigue_plot']
    
# class EntitiesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Entities
#         fields = ['name', 'race', 'type']
        
# class EntityPopulationsSerializer(serializers.ModelSerializer):
#     entity = EntitiesSerializer(source='civ_id', read_only=True)
#     class Meta:
#         model = EntityPopulations
#         fields = ['entity', 'race', 'population']
        
# class OccasionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Occasion
#         fields = ['name']
        
# class ErasSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HistoricalEras
#         fields = ['name', 'start_year', 'end_year']
        
# class EventCollectionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HistoricalEventCollections
#         fields = ['name', 'type']
        
# class RegionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Regions
#         fields = ['name', 'type']
        
# class UndergroundRegionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UndergroundRegions
#         fields = ['type', 'depth']
        
# class WorldConstructionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = WorldConstruction
#         fields = ['name', 'type']
        
# class LandmassesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Landmass
#         fields = ['name', 'coord1', 'coord2']
        
# class MountainPeaksSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MountainPeak
#         fields = ['name', 'height', 'volcano']
        
# class IntriguePlotsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = IntriguePlot
#         fields = ['type']
        
# class IdentitySerializer(serializers.ModelSerializer):
#     entity = EntitiesSerializer(source='civ_id', read_only=True)
#     nemesis = HistoricalFigureSerializer(source='nemesis_id', read_only=True)
#     class Meta:
#         model = Identities
#         fields = ['name', 'hf_id', 'birth_year', 'race', 'caste', 'profession', 'entity', 'nemesis']