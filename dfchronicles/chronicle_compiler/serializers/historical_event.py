from rest_framework import serializers
from ..models import HistoricalEvents
from .entity import EntitySerializer
from .historical_figure import HistoricalFiguresSerializer

class HistoricalEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalEvents
        fields = ['type', 'id']
        
class HistoricalEventSerializer(serializers.ModelSerializer):
    civ_id = EntitySerializer(read_only=True, many=True)
    hf_id = HistoricalFiguresSerializer(read_only=True)
    class Meta:
        model = HistoricalEvents
        fields = ['appointer_hfid', 'body_part', 'caste', 'civ_id', 'death_cause', 'feature_layer_id', 'hf_id', 'injury_type', 'link_type', 'new_job', 'old_job', 'part_lost', 'position', 'race', 'reason', 'relationship', 'site_id', 'state', 'subregion_id', 'target_hfid', 'type', 'year', 'coords', 'body_state', 'death_penalty', 'wrongful_conviction', 'crime', 'framer_hfid', 'fooled_hfid', 'convicter_enid', 'convicted_hfid', 'circumstance', 'stash_site', 'theft_method', 'structure', 'knowledge', 'first', 'link', 'position_id', 'identity', 'target_identity', 'artifact', 'occasion', 'schedule', 'attacker_civ_id', 'defender_civ_id', 'attacker_general_hfid', 'defender_general_hfid', 'subtype', 'initiating_entity', 'joining_entity', 'site_civ_id', 'dispute', 'winner_hfid', 'competitor_hfid', 'detected', 'written_content', 'returning', 'old_race', 'old_caste', 'new_race', 'new_caste', 'quality', 'identity_rep', 'target_identity_rep', 'old_account', 'new_account', 'secret_goal', 'method', 'world_construction', 'master_world_construction', 'site_property', 'last_owner', 'inherited', 'rebuilt_ruined', 'purchased_unowned', 'corruptor_seen_as', 'target_seen_as', 'successful', 'mood', 'new_site_civ', 'new_leader', 'prison_months', 'target_site', 'account_shift', 'expelled_hfids', 'shrine_amount_destroyed', 'resident_civ_id', 'position_taker_hfid', 'instigator_hfid', 'conspirator_hfid', 'actor_hfid', 'musical_form', 'poetic_form', 'dance_form', 'held_firm_in_interrogation', 'pets', 'mat', 'bodies', 'abuse_type', 'event_historical_event_collections', 'historical_event_circumstance']