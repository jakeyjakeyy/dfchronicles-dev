from rest_framework import serializers
from ..models import Sites, Structures, SiteLink, SiteProperty, HistoricalEvents, Entities, Artifact, HistoricalFigures

class HistoricalFiguresSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalFigures
        fields = ['name', 'race', 'caste', 'deity']

class ArtifactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artifact
        fields = ['name', 'name2', 'item_type', 'material', 'item_subtype', 'item_description']
    
class SiteLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteLink
        fields = ['hf_id', 'link_type', 'structure_id', ]
    
class HistoricalEventsSerializer(serializers.ModelSerializer):
    hf_id = HistoricalFiguresSerializer()
    class Meta:
        model = HistoricalEvents
        fields = ['type', 'hf_id']
        
class EntitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entities
        fields = ['name', 'type', 'race']

class SitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sites
        fields = ['name', 'type', 'id']
        
class StructuresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Structures
        fields = ['name', 'type']
        
class SitePropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteProperty
        fields = ['local_id', 'type', 'owner', 'structure_id']
        
class SiteSerializer(serializers.ModelSerializer):
    site_historical_events = HistoricalEventsSerializer(many=True)
    stash_site_historical_events = HistoricalEventsSerializer(many=True)
    target_site_id_historical_events = HistoricalEventsSerializer(many=True)
    site_link = SiteLinkSerializer(many=True)
    site_structures = StructuresSerializer(many=True)
    site_property = SitePropertySerializer(many=True)
    cur_owner_id = EntitiesSerializer()
    site_artifacts = ArtifactSerializer(many=True)
    class Meta:
        model = Sites
        fields = ['cur_owner_id', 'name', 'type', 'coords', 'rectangle', 'site_artifacts', 'attack_squad_site_historical_event_collections', 'defend_squad_site_historical_event_collections', 'site_historical_event_collections', 'site_historical_events', 'stash_site_historical_events', 'target_site_id_historical_events', 'site_link', 'site_structures', 'site_property','site_written_content_reference']