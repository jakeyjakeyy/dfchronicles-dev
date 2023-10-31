from rest_framework import serializers
from ..models import Sites, Structures, SiteLink, SiteProperty

class SiteLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteLink
        fields = ['hf_id', 'link_type', 'structure_id']
    

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
    site_link = SiteLinkSerializer(many=True)
    site_structures = StructuresSerializer(many=True)
    site_property = SitePropertySerializer(many=True)
    class Meta:
        model = Sites
        fields = ['cur_owner_id', 'name', 'type', 'coords', 'rectangle', 'site_artifacts', 'attack_squad_site_historical_event_collections', 'defend_squad_site_historical_event_collections', 'site_historical_event_collections', 'site_historical_events', 'stash_site_historical_events', 'target_site_id_historical_events', 'site_link', 'site_structures', 'site_property','site_written_content_reference']