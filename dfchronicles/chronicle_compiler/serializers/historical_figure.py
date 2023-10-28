from rest_framework import serializers
from ..models import HistoricalFigures

class HistoricalFiguresSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalFigures
        fields = ['name', 'race', 'birth_year', 'id']

class HistoricalFigureSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalFigures
        fields = ['appeared', 'associated_type', 'birth_year', 'caste', 'death_year', 'deity', 'goal', 'journey_pet', 'name', 'race', 'sphere', 'force', 'animated', 'animated_string', 'used_identity', 'ent_pop_id', 'current_identity', 'held_artifact', 'worship_hf_entities', 'hf_entity_position_assignment', 'attack_hf_historical_event_collections', 'defend_hf_historical_event_collections', 'noncom_hf_historical_event_collections', 'appointer_hf_historical_events', 'hf_historical_events', 'target_hf_historical_events', 'framer_hf_historical_events', 'fooled_hf_historical_events', 'convicted_hfid_historical_events', 'attacker_general_hfid_historical_events', 'defender_general_hfid_historical_events', 'winner_hfid_historical_events', 'competitor_hfid_historical_events', 'last_owner_historical_events', 'new_leader_historical_events', 'expelled_hfids_historical_events', 'position_taker_hfid_historical_events', 'instigator_hfid_historical_events', 'conspirator_hfid_historical_events', 'actor_hfid_historical_events', 'bodies_historical_events']
        