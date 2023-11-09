from rest_framework import serializers
from ..models import HistoricalEvents
from .entity import EntitiesSerializer
from .historical_figure import HistoricalFiguresSerializer
from .site import SitesSerializer, StructuresSerializer
from .artifact import ArtifactsSerializer
from .written_content import WrittenContentsSerializer
from .occasion import OccasionSerializer

class HistoricalEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalEvents
        fields = ['type', 'id']
        
class HistoricalEventSerializer(serializers.ModelSerializer):
    civ_id = EntitiesSerializer(read_only=True, many=True)
    perpetrator_hfid = HistoricalFiguresSerializer(read_only=True)
    appointer_hfid = HistoricalFiguresSerializer(read_only=True)
    site_id = SitesSerializer(read_only=True, many=True)
    target_hfid = HistoricalFiguresSerializer(read_only=True)
    framer_hfid = HistoricalFiguresSerializer(read_only=True)
    fooled_hfid = HistoricalFiguresSerializer(read_only=True)
    convicter_enid = EntitiesSerializer(read_only=True)
    convicted_hfid = HistoricalFiguresSerializer(read_only=True)
    stash_site = SitesSerializer(read_only=True)
    structure = StructuresSerializer(read_only=True)
    attacker_civ_id = EntitiesSerializer(read_only=True)
    artifact = ArtifactsSerializer(read_only=True)
    defender_civ_id = EntitiesSerializer(read_only=True,)
    attacker_general_hfid = HistoricalFiguresSerializer(read_only=True)
    defender_general_hfid = HistoricalFiguresSerializer(read_only=True)
    initiating_entity = EntitiesSerializer(read_only=True)
    joining_entity = EntitiesSerializer(read_only=True, many=True)
    site_civ_id = EntitiesSerializer(read_only=True)
    winner_hfid = HistoricalFiguresSerializer(read_only=True)
    competitor_hfid = HistoricalFiguresSerializer(read_only=True)
    written_content = WrittenContentsSerializer(read_only=True)
    last_owner = HistoricalFiguresSerializer(read_only=True)
    new_site_civ = EntitiesSerializer(read_only=True)
    new_leader = HistoricalFiguresSerializer(read_only=True)
    target_site = SitesSerializer(read_only=True)
    expelled_hfids = HistoricalFiguresSerializer(read_only=True, many=True)
    resident_civ_id = EntitiesSerializer(read_only=True)
    position_taker_hfid = HistoricalFiguresSerializer(read_only=True)
    instigator_hfid = HistoricalFiguresSerializer(read_only=True)
    conspirator_hfid = HistoricalFiguresSerializer(read_only=True)
    # actor_hfid = HistoricalFiguresSerializer(read_only=True)
    bodies = HistoricalFiguresSerializer(read_only=True, many=True)
    occasion = OccasionSerializer(read_only=True)

    class Meta:
        model = HistoricalEvents
        fields = ['appointer_hfid', 'body_part', 'caste', 'civ_id', 'death_cause', 'feature_layer_id', 'perpetrator_hfid', 'injury_type', 'link_type', 'new_job', 'old_job', 'part_lost', 'position', 'race', 'reason', 'relationship', 'site_id', 'state', 'subregion_id', 'target_hfid', 'type', 'year', 'coords', 'body_state', 'death_penalty', 'wrongful_conviction', 'crime', 'framer_hfid', 'fooled_hfid', 'convicter_enid', 'convicted_hfid', 'circumstance', 'stash_site', 'theft_method', 'structure', 'knowledge', 'first', 'link', 'position_id', 'identity', 'target_identity', 'artifact', 'occasion', 'schedule', 'attacker_civ_id', 'defender_civ_id', 'attacker_general_hfid', 'defender_general_hfid', 'subtype', 'initiating_entity', 'joining_entity', 'site_civ_id', 'dispute', 'winner_hfid', 'competitor_hfid', 'detected', 'written_content', 'returning', 'old_race', 'old_caste', 'new_race', 'new_caste', 'quality', 'identity_rep', 'target_identity_rep', 'old_account', 'new_account', 'secret_goal', 'method', 'world_construction', 'master_world_construction', 'site_property', 'last_owner', 'inherited', 'rebuilt_ruined', 'purchased_unowned', 'corruptor_seen_as', 'target_seen_as', 'successful', 'mood', 'new_site_civ', 'new_leader', 'prison_months', 'target_site', 'account_shift', 'expelled_hfids', 'shrine_amount_destroyed', 'resident_civ_id', 'position_taker_hfid', 'instigator_hfid', 'conspirator_hfid', 'actor_hfid', 'musical_form', 'poetic_form', 'dance_form', 'held_firm_in_interrogation', 'pets', 'mat', 'bodies', 'abuse_type', 'event_historical_event_collections', 'historical_event_circumstance']