from rest_framework import serializers
from ..models import Entities

class EntitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entities
        fields = ['name', 'race', 'type', 'id']
        
class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entities
        fields = ['name', 'race', 'type', 'profession', 'weapon', 'worship_id', 'civ_entity_position', 'entity_position_assignment', 'occasion', 'attack_historical_event_collections', 'defend_historical_event_collections', 'historical_event_collections', 'target_historical_event_collections', 'civ_historical_events', 'convicter_enid_historical_events', 'target_enid_historical_events', 'attacker_civ_historical_events', 'defender_civ_historical_events', 'initiating_entity_historical_events', 'joining_entity_historical_events', 'site_civ_id_historical_events', 'new_site_civ_historical_events', 'resident_civ_historical_events', 'civ_entity_link', 'civ_site_link', 'civ_sites', 'owned_sites', 'civ_structures', 'civ_intrigue_plot', 'civ_intrigue_actor', 'civ_entity_former_position_link', 'civ_identities', 'civ_entity_position_link', 'civ_entity_squad_link']