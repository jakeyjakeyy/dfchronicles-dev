from rest_framework import serializers
from ..models import HistoricalEventCollections
from .historical_event import HistoricalEventSerializer
from .entity import EntitiesSerializer
from .historical_figure import HistoricalFiguresSerializer
from .occasion import OccasionsSerializer
from .world import WorldsSerializer


class EventCollectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalEventCollections
        fields = ["name", "type", "id"]


class EventCollectionSerializer(serializers.ModelSerializer):
    aggressor_entity_id = EntitiesSerializer(read_only=True)
    attacking_hfid = HistoricalFiguresSerializer(read_only=True, many=True)
    attacking_squad_site = EntitiesSerializer(read_only=True)
    defender_entity_id = EntitiesSerializer(read_only=True)
    defending_hfid = HistoricalFiguresSerializer(read_only=True, many=True)
    defending_squad_site = EntitiesSerializer(read_only=True)
    civ_id = EntitiesSerializer(read_only=True)
    noncom_hfid = HistoricalFiguresSerializer(read_only=True)
    site_id = EntitiesSerializer(read_only=True)
    target_entity_id = EntitiesSerializer(read_only=True)
    event = HistoricalEventSerializer(read_only=True, many=True)
    world = WorldsSerializer(read_only=True)
    # occasion_id = OccasionsSerializer(read_only=True) LINK OCCASION IN MODELS
    # event_collection = EventCollectionSerializer(read_only=True, many=True)
    class Meta:
        model = HistoricalEventCollections
        fields = [
            "world",
            "aggressor_entity_id",
            "attacking_hfid",
            "attacking_squad_is_undead",
            "attacking_squad_deaths",
            "attacking_squad_number",
            "attacking_squad_race",
            "attacking_squad_site",
            "defender_entity_id",
            "defending_hfid",
            "defending_squad_is_undead",
            "defending_squad_deaths",
            "defending_squad_number",
            "defending_squad_race",
            "defending_squad_site",
            "civ_id",
            "coords",
            "end_year",
            "event",
            "name",
            "noncom_hfid",
            "occasion_id",
            "outcome",
            "site_id",
            "start_year",
            "subregion_id",
            "target_entity_id",
            "type",
            "hist_event_collection_circumstance",
            "event_collection",
            "id"
        ]
