from rest_framework import serializers
from ..models import HistoricalEventCollections

class EventCollectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalEventCollections
        fields = ['name', 'type', 'id']
        
class EventCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalEventCollections
        fields = ['aggressor_entity_id', 'attacking_hfid', 'attacking_squad_animated', 'attacking_squad_deaths','attacking_squad_number', 'attacking_squad_race', 'attacking_squad_site', 'defender_entity_id', 'defending_hfid', 'defending_squad_animated', 'defending_squad_deaths', 'defending_squad_number', 'defending_squad_race', 'defending_squad_site', 'civ_id', 'coords', 'end_year', 'event', 'name', 'noncom_hfid', 'occasion_id', 'outcome', 'site_id', 'start_year', 'subregion_id', 'target_entity_id', 'type', 'hist_event_collection_circumstance']