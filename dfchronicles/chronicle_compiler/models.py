# Sample django models
from django.db import models


class Artifact(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    site_id = models.IntegerField()
    holder_id = models.ForeignKey('HistoricalFigures', null=True, related_name='hf_artifacts', on_delete=models.SET_NULL)
    name_string = models.CharField(max_length=100)
    page_number = models.IntegerField(null=True)
    written_content_id = models.ForeignKey('WrittenContents', null=True, related_name='written_artifacts', on_delete=models.SET_NULL)
    item_type = models.CharField(max_length=100)
    writing = models.IntegerField(null=True)
    material = models.CharField(max_length=100)
    item_subtype = models.CharField(max_length=100, null=True)
    item_description = models.CharField(max_length=100, null=True)

class Entities(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, null=True)
    race = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100)
    hf_id = models.ManyToManyField('HistoricalFigures', related_name='entities')


class EntityPosition(models.Model):
    position_id = models.IntegerField()
    entity_id = models.ForeignKey('Entities', related_name='entity_position', null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    name_male = models.CharField(max_length=100, null=True)
    name_female = models.CharField(max_length=100, null=True)
    spouse = models.CharField(max_length=100, null=True)
    spouse_male = models.CharField(max_length=100, null=True)
    spouse_female = models.CharField(max_length=100, null=True)

class EntityPositionAssignment(models.Model):
    position_id = models.ForeignKey('EntityPosition', related_name='entity_position_assignment', null=True, on_delete=models.SET_NULL)
    historical_figure_id = models.ForeignKey('HistoricalFigures', related_name='hf_entity_position_assignment', null=True, on_delete=models.SET_NULL)

class EntityPopulations(models.Model):
    civ_id = models.ForeignKey('Entities', related_name='entity_populations', null=True, on_delete=models.SET_NULL)
    # race and pop aren't separated in the XML
    # I imagine this will be easier to split on entity creation
    race = models.CharField(max_length=100)
    population = models.IntegerField()

class Occasion(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True)
    site_id = models.ForeignKey('Sites', related_name='occasion', null=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=100)

class Schedule(models.Model):
    type = models.CharField(max_length=100)
    reference = models.ForeignKey('WrittenContents', related_name='schedule', null=True, on_delete=models.SET_NULL)
    item_type = models.CharField(max_length=100, null=True)
    item_subtype = models.CharField(max_length=100, null=True)

class Feature(models.Model):
    type = models.CharField(max_length=100)
    reference = models.ForeignKey('WrittenContents', related_name='feature', null=True, on_delete=models.SET_NULL)

# I imagine this has more data, need a larger sample to confirm
class HistoricalEras(models.Model):
    name = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True)

class HistoricalEventCollections(models.Model):
    aggressor_entity_id = models.ForeignKey('Entities', related_name='attack_historical_event_collections', null=True, on_delete=models.SET_NULL)
    attacking_hfid = models.ForeignKey('HistoricalFigures', related_name='attack_hf_historical_event_collections', null=True, on_delete=models.SET_NULL)
    attacking_squad_deaths = models.IntegerField(null=True)
    attacking_squad_entity_pop = models.IntegerField(null=True)
    attacking_squad_number = models.IntegerField(null=True)
    attacking_squad_race = models.CharField(max_length=100, null=True)
    attacking_squad_site = models.ForeignKey('Sites', related_name='attack_squad_site_historical_event_collections', null=True, on_delete=models.SET_NULL)
    defender_entity_id = models.ForeignKey('Entities', related_name='defend_historical_event_collections', null=True, on_delete=models.SET_NULL)
    defending_hfid = models.ForeignKey('HistoricalFigures', related_name='defend_hf_historical_event_collections', null=True, on_delete=models.SET_NULL)
    defending_squad_deaths = models.IntegerField(null=True)
    defending_squad_entity_pop = models.IntegerField(null=True)
    defending_squad_number = models.IntegerField(null=True)
    defending_squad_race = models.CharField(max_length=100, null=True)
    defending_squad_site = models.ForeignKey('Sites', related_name='defend_squad_site_historical_event_collections', null=True, on_delete=models.SET_NULL)
    civ_id = models.ForeignKey('Entities', related_name='historical_event_collections', null=True, on_delete=models.SET_NULL)
    end_year = models.IntegerField(null=True)
    # Not sure what event is
    event = models.CharField(max_length=100)
    # Not sure what eventcol is
    eventcol = models.IntegerField(null=True)
    feature_layer_id = models.IntegerField(null=True)
    name = models.CharField(max_length=100, null=True)
    occasion_id = models.IntegerField(null=True)
    outcome = models.CharField(max_length=100, null=True)
    site_id = models.ForeignKey('Sites', related_name='site_historical_event_collections', null=True, on_delete=models.SET_NULL)
    start_year = models.IntegerField(null=True)
    subregion_id = models.IntegerField(null=True)
    type = models.CharField(max_length=100, null=True)
    # Not sure what war_eventcol is
    war_eventcol = models.IntegerField(null=True)

class HistoricalEvents(models.Model):
    # Not sure what feature_layer_id is
    appointer_hfid = models.ForeignKey('HistoricalFigures', related_name='appointer_hf_historical_events', null=True, on_delete=models.SET_NULL)
    civ_id = models.ForeignKey('Entities', related_name='civ_historical_events', null=True, on_delete=models.SET_NULL)
    feature_layer_id = models.IntegerField(null=True)
    hf_id = models.ForeignKey('HistoricalFigures', related_name='hf_historical_events', null=True, on_delete=models.SET_NULL)
    id = models.IntegerField(primary_key=True, unique=True)
    link_type = models.CharField(max_length=100, null=True)
    promise_to_hfid = models.ForeignKey('HistoricalFigures', related_name='promise_hf_historical_events', null=True, on_delete=models.SET_NULL)
    reason = models.CharField(max_length=100, null=True)
    site_id = models.ForeignKey('Sites', related_name='site_historical_events', null=True, on_delete=models.SET_NULL)
    state = models.CharField(max_length=100, null=True)
    subregion_id = models.IntegerField(null=True)
    type = models.CharField(max_length=100, null=True)
    year = models.IntegerField(null=True)

class HistoricalEventRelationships(models.Model):
    # id = event from XML
    id = models.IntegerField(primary_key=True, unique=True)
    relationship = models.CharField(max_length=100, null=True)
    source_hfid = models.ForeignKey('HistoricalFigures', related_name='source_hf_historical_event_relationships', null=True, on_delete=models.SET_NULL)
    target_hfid = models.ForeignKey('HistoricalFigures', related_name='target_hf_historical_event_relationships', null=True, on_delete=models.SET_NULL)
    year = models.IntegerField(null=True)

class HistoricalFigures(models.Model):
    appeared = models.IntegerField(null=True)
    associated_type = models.CharField(max_length=100, null=True)
    birth_year = models.IntegerField(null=True)
    caste = models.CharField(max_length=100, null=True)
    death_year = models.IntegerField(null=True)
    goal = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    race = models.CharField(max_length=100, null=True)
    sphere = models.CharField(max_length=100, null=True)
    used_identity = models.ForeignKey('Identities', related_name='used_identity_historical_figures', null=True, on_delete=models.SET_NULL)

class EntityLink(models.Model):
    civ_id = models.ForeignKey('Entities', related_name='entity_link', null=True, on_delete=models.SET_NULL)
    hf_id = models.ForeignKey('HistoricalFigures', related_name='entity_link', null=True, on_delete=models.SET_NULL)
    link_type = models.CharField(max_length=100, null=True)

class SiteLink(models.Model):
    civ_id = models.ForeignKey('Entities', related_name='civ_site_link', null=True, on_delete=models.SET_NULL)
    hf_id = models.ForeignKey('HistoricalFigures', related_name='hf_site_link', null=True, on_delete=models.SET_NULL)
    link_type = models.CharField(max_length=100, null=True)
    site_id = models.ForeignKey('Sites', related_name='site_link', null=True, on_delete=models.SET_NULL)

class HfSkill(models.Model):
    hf_id = models.ForeignKey('HistoricalFigures', related_name='hf_skill', null=True, on_delete=models.SET_NULL)
    skill = models.CharField(max_length=100, null=True)
    total_ip = models.IntegerField(null=True)

class HfLink(models.Model):
    hf_origin_id = models.ForeignKey('HistoricalFigures', related_name='hf_link', null=True, on_delete=models.SET_NULL)
    hf_id = models.ForeignKey('HistoricalFigures', related_name='hf_link_target', null=True, on_delete=models.SET_NULL)
    link_type = models.CharField(max_length=100, null=True)
    link_strength = models.IntegerField(null=True)

class Regions(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    evilness = models.CharField(max_length=100, null=True)

class Sites(models.Model):
    civ_id = models.ForeignKey('Entities', related_name='civ_sites', null=True, on_delete=models.SET_NULL)
    cur_owner_id = models.ForeignKey('Entities', related_name='owned_sites', null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

class Structures(models.Model):
    site_id = models.ForeignKey('Sites', related_name='site_structures', null=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)
    name2 = models.CharField(max_length=100, null=True)
    inhabitant = models.ForeignKey('HistoricalFigures', related_name='inhabitant_structures', null=True, on_delete=models.SET_NULL)

class UndergroundRegions(models.Model):
    type = models.CharField(max_length=100)
    depth = models.IntegerField(null=True)

class WrittenContents(models.Model):
    author_hfid = models.ForeignKey('HistoricalFigures', related_name='written_contents', null=True, on_delete=models.SET_NULL)
    form = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    style = models.CharField(max_length=100, null=True)
    reference = models.ForeignKey('WrittenContents', related_name='reference_written_contents', null=True, on_delete=models.SET_NULL)

class IntrigueActor(models.Model):
    source_hfid = models.ForeignKey('HistoricalFigures', related_name='source_intrigue_actor', null=True, on_delete=models.SET_NULL)
    target_hfid = models.ForeignKey('HistoricalFigures', related_name='target_intrigue_actor', null=True, on_delete=models.SET_NULL)
    role = models.CharField(max_length=100, null=True)
    strategy = models.CharField(max_length=100, null=True)

class RelationshipProfileVisual(models.Model):
    source_hfid = models.ForeignKey('HistoricalFigures', related_name='source_relationship_profile_visual', null=True, on_delete=models.SET_NULL)
    target_hfid = models.ForeignKey('HistoricalFigures', related_name='target_relationship_profile_visual', null=True, on_delete=models.SET_NULL)
    fear = models.IntegerField(null=True)
    last_meet_year = models.IntegerField(null=True)
    love = models.IntegerField(null=True)
    loyalty = models.IntegerField(null=True)
    meet_count = models.IntegerField(null=True)
    respect = models.IntegerField(null=True)
    trust = models.IntegerField(null=True)

class EntityFormerPositionLink(models.Model):
    civ_id = models.ForeignKey('Entities', related_name='civ_entity_former_position_link', null=True, on_delete=models.SET_NULL)
    end_year = models.IntegerField(null=True)
    hf_id = models.ForeignKey('HistoricalFigures', related_name='hf_entity_former_position_link', null=True, on_delete=models.SET_NULL)
    position_id = models.ForeignKey('EntityPosition', related_name='entity_former_position_link', null=True, on_delete=models.SET_NULL)
    start_year = models.IntegerField(null=True)

class Identities(models.Model):
    name = models.CharField(max_length=100)
    hf_id = models.ForeignKey('HistoricalFigures', related_name='identities', null=True, on_delete=models.SET_NULL)
    birth_year = models.IntegerField(null=True)
    civ_id = models.ForeignKey('Entities', related_name='civ_identities', null=True, on_delete=models.SET_NULL)
    nemesis = models.ForeignKey('HistoricalFigures', related_name='nemesis_identities', null=True, on_delete=models.SET_NULL)
    race = models.CharField(max_length=100, null=True)
    caste = models.CharField(max_length=100, null=True)
    profession = models.CharField(max_length=100, null=True)