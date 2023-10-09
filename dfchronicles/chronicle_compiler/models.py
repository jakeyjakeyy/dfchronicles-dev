from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class World(models.Model):
    name = models.CharField(max_length=500)
    name2 = models.CharField(max_length=500, null=True)
    owner = models.ForeignKey(User, related_name='worlds', null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f"{self.id} | {self.name} | {self.owner}"

class Artifact(models.Model):
    world = models.ForeignKey('World', related_name='world_artifacts', null=True, on_delete=models.CASCADE)
    chronicle_id = models.IntegerField()
    name = models.CharField(max_length=500, null=True)
    name2 = models.CharField(max_length=500, null=True)
    site_id = models.ForeignKey('Sites', related_name='site_artifacts', null=True, on_delete=models.SET_NULL)
    holder_id = models.ForeignKey('HistoricalFigures', null=True, related_name='hf_artifacts', on_delete=models.SET_NULL)
    page_number = models.IntegerField(null=True)
    written_content_id = models.ForeignKey('WrittenContents', null=True, related_name='written_artifacts', on_delete=models.SET_NULL)
    item_type = models.CharField(max_length=500, null=True)
    material = models.CharField(max_length=500, null=True)
    item_subtype = models.CharField(max_length=500, null=True)
    item_description = models.CharField(max_length=500, null=True)
    structure_local_id = models.ForeignKey('Structures', null=True, related_name='structure_artifacts', on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name} | {self.world}"

class Entities(models.Model):
    world = models.ForeignKey('World', related_name='world_entities', null=True, on_delete=models.CASCADE)
    chronicle_id = models.IntegerField()
    name = models.CharField(max_length=500, null=True)
    race = models.CharField(max_length=500, null=True)
    type = models.CharField(max_length=500)
    profession = models.CharField(max_length=500, null=True)
    weapon = models.CharField(max_length=500, null=True)
    worship_id = models.ForeignKey('HistoricalFigures', related_name='worship_hf_entities', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name} | {self.world}"

class EntityPosition(models.Model):
    world = models.ForeignKey('World', related_name='world_entity_position', null=True, on_delete=models.CASCADE)
    civ_position_id = models.IntegerField()
    civ_id = models.ForeignKey('Entities', related_name='civ_entity_position', null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=500)
    name_male = models.CharField(max_length=500, null=True)
    name_female = models.CharField(max_length=500, null=True)
    spouse = models.CharField(max_length=500, null=True)
    spouse_male = models.CharField(max_length=500, null=True)
    spouse_female = models.CharField(max_length=500, null=True)

class EntityPositionAssignment(models.Model):
    world = models.ForeignKey('World', related_name='world_entity_position_assignment', null=True, on_delete=models.CASCADE)
    civ_position_assignment_id = models.IntegerField()
    civ_id = models.ForeignKey('Entities', related_name='entity_position_assignment', null=True, on_delete=models.SET_NULL)
    position_id = models.ForeignKey('EntityPosition', related_name='entity_position_assignment', null=True, on_delete=models.SET_NULL)
    hf_id = models.ForeignKey('HistoricalFigures', related_name='hf_entity_position_assignment', null=True, on_delete=models.SET_NULL)
    squad_id = models.IntegerField(null=True)

class EntityPopulations(models.Model):
    world = models.ForeignKey('World', related_name='world_entity_populations', null=True, on_delete=models.CASCADE)
    chronicle_id = models.IntegerField()
    civ_id = models.ForeignKey('Entities', related_name='entity_populations', null=True, on_delete=models.SET_NULL)
    # race and pop aren't separated in the XML
    # I imagine this will be easier to split on entity creation
    race = models.CharField(max_length=500, null=True)
    population = models.IntegerField(null=True)

class Occasion(models.Model):
    world = models.ForeignKey('World', related_name='world_occasion', null=True, on_delete=models.CASCADE)
    civ_occasion_id = models.IntegerField()
    civ_id = models.ForeignKey('Entities', related_name='occasion', null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=500)

class Schedule(models.Model):
    world = models.ForeignKey('World', related_name='world_schedules', null=True, on_delete=models.CASCADE)
    occasion_schedule_id = models.IntegerField()
    occasion = models.ForeignKey('Occasion', related_name='occasion_schedule', null=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=500)
    reference = models.ForeignKey('WrittenContents', related_name='schedule', null=True, on_delete=models.SET_NULL)
    item_type = models.CharField(max_length=500, null=True)
    item_subtype = models.CharField(max_length=500, null=True)

class Feature(models.Model):
    world = models.ForeignKey('World', related_name='world_feature', null=True, on_delete=models.CASCADE)
    schedule = models.ForeignKey('Schedule', related_name='schedule_feature', null=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=500)
    reference = models.ForeignKey('WrittenContents', related_name='feature', null=True, on_delete=models.SET_NULL)

# I imagine this has more data, need a larger sample to confirm
class HistoricalEras(models.Model):
    world = models.ForeignKey('World', related_name='world_historical_eras', null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True)

class HistoricalEventCollections(models.Model):
    world = models.ForeignKey('World', related_name='world_historical_event_collections', null=True, on_delete=models.CASCADE)
    chronicle_id = models.IntegerField()
    aggressor_entity_id = models.ForeignKey('Entities', related_name='attack_historical_event_collections', null=True, on_delete=models.SET_NULL)
    attacking_hfid = models.ManyToManyField('HistoricalFigures', related_name='attack_hf_historical_event_collections')
    attacking_squad_animated = models.BooleanField(null=True, default=False)
    attacking_squad_deaths = models.IntegerField(null=True)
    attacking_squad_number = models.IntegerField(null=True)
    attacking_squad_race = models.CharField(max_length=1000, null=True)
    attacking_squad_site = models.ForeignKey('Sites', related_name='attack_squad_site_historical_event_collections', null=True, on_delete=models.SET_NULL)
    defender_entity_id = models.ForeignKey('Entities', related_name='defend_historical_event_collections', null=True, on_delete=models.SET_NULL)
    defending_hfid = models.ManyToManyField('HistoricalFigures', related_name='defend_hf_historical_event_collections')
    defending_squad_animated = models.BooleanField(null=True, default=False)
    defending_squad_deaths = models.IntegerField(null=True)
    defending_squad_number = models.IntegerField(null=True)
    defending_squad_race = models.CharField(max_length=1000, null=True)
    defending_squad_site = models.ForeignKey('Sites', related_name='defend_squad_site_historical_event_collections', null=True, on_delete=models.SET_NULL)
    civ_id = models.ForeignKey('Entities', related_name='historical_event_collections', null=True, on_delete=models.SET_NULL)
    coords = models.CharField(max_length=500, null=True)
    end_year = models.IntegerField(null=True)
    event = models.ManyToManyField('HistoricalEvents', related_name='event_historical_event_collections')
    name = models.CharField(max_length=500, null=True)
    noncom_hfid = models.ManyToManyField('HistoricalFigures', related_name='noncom_hf_historical_event_collections')
    occasion_id = models.IntegerField(null=True)
    outcome = models.CharField(max_length=500, null=True)
    site_id = models.ForeignKey('Sites', related_name='site_historical_event_collections', null=True, on_delete=models.SET_NULL)
    start_year = models.IntegerField(null=True)
    subregion_id = models.IntegerField(null=True)
    target_entity_id = models.ForeignKey('Entities', related_name='target_historical_event_collections', null=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=500, null=True)

class HistoricalEvents(models.Model):
    world = models.ForeignKey('World', related_name='world_historical_events', null=True, on_delete=models.CASCADE)
    chronicle_id = models.IntegerField()
    appointer_hfid = models.ForeignKey('HistoricalFigures', related_name='appointer_hf_historical_events', null=True, on_delete=models.SET_NULL)
    body_part = models.IntegerField(null=True)
    caste = models.CharField(max_length=500, null=True)
    civ_id = models.ForeignKey('Entities', related_name='civ_historical_events', null=True, on_delete=models.SET_NULL)
    death_cause = models.CharField(max_length=500, null=True)
    # Not sure what feature_layer_id is
    feature_layer_id = models.IntegerField(null=True)
    hf_id = models.ForeignKey('HistoricalFigures', related_name='hf_historical_events', null=True, on_delete=models.SET_NULL)
    injury_type = models.CharField(max_length=500, null=True)
    link_type = models.CharField(max_length=500, null=True)
    new_job = models.CharField(max_length=500, null=True)
    old_job = models.CharField(max_length=500, null=True)
    part_lost = models.BooleanField(null=True)
    position = models.CharField(max_length=500, null=True)
    promise_to_hfid = models.ForeignKey('HistoricalFigures', related_name='promise_hf_historical_events', null=True, on_delete=models.SET_NULL)
    race = models.CharField(max_length=500, null=True)
    reason = models.CharField(max_length=500, null=True)
    relationship = models.CharField(max_length=500, null=True)
    site_id = models.ForeignKey('Sites', related_name='site_historical_events', null=True, on_delete=models.SET_NULL)
    state = models.CharField(max_length=500, null=True)
    subregion_id = models.IntegerField(null=True)
    target_hfid = models.ForeignKey('HistoricalFigures', related_name='target_hf_historical_events', null=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=500, null=True)
    year = models.IntegerField(null=True)

class Circumstance(models.Model):
    world = models.ForeignKey('World', related_name='world_circumstance', null=True, on_delete=models.CASCADE)
    historical_event = models.ForeignKey('HistoricalEvents', related_name='historical_event_circumstance', null=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=500)
    hist_event_id = models.ManyToManyField('HistoricalEvents', related_name='hist_event_circumstance')
    hist_event_collection = models.ForeignKey('HistoricalEventCollections', related_name='hist_event_collection_circumstance', null=True, on_delete=models.SET_NULL)

class HistoricalFigures(models.Model):
    world = models.ForeignKey('World', related_name='world_historical_figures', null=True, on_delete=models.CASCADE)
    chronicle_id = models.IntegerField()
    appeared = models.IntegerField(null=True)
    associated_type = models.CharField(max_length=500, null=True)
    birth_year = models.IntegerField(null=True)
    caste = models.CharField(max_length=500, null=True)
    death_year = models.IntegerField(null=True)
    deity = models.BooleanField(null=True, default=False)
    goal = models.CharField(max_length=500, null=True)
    journey_pet = models.CharField(max_length=500, null=True)
    name = models.CharField(max_length=500, null=True)
    race = models.CharField(max_length=500, null=True)
    sphere = models.CharField(max_length=500, null=True)
    used_identity = models.ManyToManyField('Identities', related_name='used_identity_historical_figures')
    ent_pop_id = models.ForeignKey('EntityPopulations', related_name='ent_pop_historical_figures', null=True, on_delete=models.SET_NULL)
    current_identity = models.ForeignKey('Identities', related_name='current_identity_historical_figures', null=True, on_delete=models.SET_NULL)
    held_artifact = models.ManyToManyField('Artifact', related_name='holds_artifact_historical_figures')
    force = models.BooleanField(null=True, default=False)
    animated = models.BooleanField(null=True, default=False)
    animated_string = models.CharField(max_length=500, null=True)

# links historical figures to civs
class EntityLink(models.Model):
    world = models.ForeignKey('World', related_name='world_entity_link', null=True, on_delete=models.CASCADE)
    civ_id = models.ForeignKey('Entities', related_name='civ_entity_link', null=True, on_delete=models.SET_NULL)
    hf_id = models.ForeignKey('HistoricalFigures', related_name='hf_entity_link', null=True, on_delete=models.SET_NULL)
    link_type = models.CharField(max_length=500, null=True)
    link_strength = models.IntegerField(null=True)

# seems to link lairs to historical figures
class SiteLink(models.Model):
    world = models.ForeignKey('World', related_name='world_site_link', null=True, on_delete=models.CASCADE)
    civ_id = models.ForeignKey('Entities', related_name='civ_site_link', null=True, on_delete=models.SET_NULL)
    hf_id = models.ForeignKey('HistoricalFigures', related_name='hf_site_link', null=True, on_delete=models.SET_NULL)
    link_type = models.CharField(max_length=500, null=True)
    site_id = models.ForeignKey('Sites', related_name='site_link', null=True, on_delete=models.SET_NULL)
    structure_id = models.ForeignKey('Structures', related_name='structure_link', null=True, on_delete=models.SET_NULL)

class HfSkill(models.Model):
    world = models.ForeignKey('World', related_name='world_hf_skill', null=True, on_delete=models.CASCADE)
    hf_id = models.ForeignKey('HistoricalFigures', related_name='hf_skill', null=True, on_delete=models.SET_NULL)
    skill = models.CharField(max_length=500, null=True)
    total_ip = models.IntegerField(null=True)

class HfLink(models.Model):
    world = models.ForeignKey('World', related_name='world_hf_link', null=True, on_delete=models.CASCADE)
    hf_origin_id = models.ForeignKey('HistoricalFigures', related_name='hf_link', null=True, on_delete=models.SET_NULL)
    hf_id = models.ForeignKey('HistoricalFigures', related_name='hf_link_target', null=True, on_delete=models.SET_NULL)
    link_type = models.CharField(max_length=500, null=True)
    link_strength = models.IntegerField(null=True)

class Regions(models.Model):
    world = models.ForeignKey('World', related_name='world_regions', null=True, on_delete=models.CASCADE)
    chronicle_id = models.IntegerField()
    name = models.CharField(max_length=500)
    type = models.CharField(max_length=500)
    evilness = models.CharField(max_length=500, null=True)

class Sites(models.Model):
    world = models.ForeignKey('World', related_name='world_sites', null=True, on_delete=models.CASCADE)
    chronicle_id = models.IntegerField()
    civ_id = models.ForeignKey('Entities', related_name='civ_sites', null=True, on_delete=models.SET_NULL)
    cur_owner_id = models.ForeignKey('Entities', related_name='owned_sites', null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=500)
    type = models.CharField(max_length=500)

class Structures(models.Model):
    world = models.ForeignKey('World', related_name='world_structures', null=True, on_delete=models.CASCADE)
    site_id = models.ForeignKey('Sites', related_name='site_structures', null=True, on_delete=models.SET_NULL)
    structure_id = models.IntegerField()
    type = models.CharField(max_length=500)
    name = models.CharField(max_length=500, null=True)
    name2 = models.CharField(max_length=500, null=True)
    inhabitant = models.ForeignKey('HistoricalFigures', related_name='inhabitant_structures', null=True, on_delete=models.SET_NULL)

class SiteProperty(models.Model):
    world = models.ForeignKey('World', related_name='world_site_property', null=True, on_delete=models.CASCADE)
    site_id = models.ForeignKey('Sites', related_name='site_property', null=True, on_delete=models.SET_NULL)
    local_id = models.IntegerField()
    type = models.CharField(max_length=500)
    owner = models.ForeignKey('HistoricalFigures', related_name='owner_site_property', null=True, on_delete=models.SET_NULL)

class UndergroundRegions(models.Model):
    world = models.ForeignKey('World', related_name='world_underground_regions', null=True, on_delete=models.CASCADE)
    chronicle_id = models.IntegerField()
    type = models.CharField(max_length=500)
    depth = models.IntegerField(null=True)

class WrittenContents(models.Model):
    world = models.ForeignKey('World', related_name='world_written_contents', null=True, on_delete=models.CASCADE)
    chronicle_id = models.IntegerField()
    author_hfid = models.ForeignKey('HistoricalFigures', related_name='written_contents', null=True, on_delete=models.SET_NULL)
    form = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    style = models.CharField(max_length=500, null=True)
    reference = models.ForeignKey('WrittenContents', related_name='reference_written_contents', null=True, on_delete=models.SET_NULL)

class IntriguePlot(models.Model):
    world = models.ForeignKey('World', related_name='world_intrigue_plot', null=True, on_delete=models.CASCADE)
    civ_id = models.ForeignKey('Entities', related_name='civ_intrigue_plot', null=True, on_delete=models.SET_NULL)
    local_id = models.IntegerField()
    source_hfid = models.ForeignKey('HistoricalFigures', related_name='source_intrigue_plot', null=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=500, null=True)
    on_hold = models.BooleanField(null=True, default=False)
    artifact = models.ForeignKey('Artifact', related_name='artifact_intrigue_plot', null=True, on_delete=models.SET_NULL)
    delegated_plot_hfid = models.ForeignKey('HistoricalFigures', related_name='delegated_plot_hfid_intrigue_plot', null=True, on_delete=models.SET_NULL)

class IntrigueActor(models.Model):
    world = models.ForeignKey('World', related_name='world_intrigue_actor', null=True, on_delete=models.CASCADE)
    local_id = models.IntegerField()
    source_hfid = models.ForeignKey('HistoricalFigures', related_name='source_intrigue_actor', null=True, on_delete=models.SET_NULL)
    target_hfid = models.ForeignKey('HistoricalFigures', related_name='target_intrigue_actor', null=True, on_delete=models.SET_NULL)
    role = models.CharField(max_length=500, null=True)
    strategy = models.CharField(max_length=500, null=True)
    civ_id = models.ForeignKey('Entities', related_name='civ_intrigue_actor', null=True, on_delete=models.SET_NULL)
    promised_actor_immortality = models.BooleanField(null=True, default=False)
    promised_me_immortality = models.BooleanField(null=True, default=False)


class RelationshipProfileVisual(models.Model):
    world = models.ForeignKey('World', related_name='world_relationship_profile_visual', null=True, on_delete=models.CASCADE)
    source_hfid = models.ForeignKey('HistoricalFigures', related_name='source_relationship_profile_visual', null=True, on_delete=models.SET_NULL)
    target_hfid = models.ForeignKey('HistoricalFigures', related_name='target_relationship_profile_visual', null=True, on_delete=models.SET_NULL)
    fear = models.IntegerField(null=True)
    last_meet_year = models.IntegerField(null=True)
    love = models.IntegerField(null=True)
    loyalty = models.IntegerField(null=True)
    meet_count = models.IntegerField(null=True)
    respect = models.IntegerField(null=True)
    trust = models.IntegerField(null=True)
    known_identity = models.ForeignKey('Identities', related_name='known_identity_relationship_profile_visual', null=True, on_delete=models.SET_NULL)
    rep_friendly = models.IntegerField(null=True)
    rep_information_source = models.IntegerField(null=True)

class EntityFormerPositionLink(models.Model):
    world = models.ForeignKey('World', related_name='world_entity_former_position_link', null=True, on_delete=models.CASCADE)
    civ_id = models.ForeignKey('Entities', related_name='civ_entity_former_position_link', null=True, on_delete=models.SET_NULL)
    end_year = models.IntegerField(null=True)
    hf_id = models.ForeignKey('HistoricalFigures', related_name='hf_entity_former_position_link', null=True, on_delete=models.SET_NULL)
    position_id = models.ForeignKey('EntityPosition', related_name='entity_former_position_link', null=True, on_delete=models.SET_NULL)
    start_year = models.IntegerField(null=True)

class Identities(models.Model):
    world = models.ForeignKey('World', related_name='world_identities', null=True, on_delete=models.CASCADE)
    chronicle_id = models.IntegerField()
    name = models.CharField(max_length=500)
    hf_id = models.ForeignKey('HistoricalFigures', related_name='identities', null=True, on_delete=models.SET_NULL)
    birth_year = models.IntegerField(null=True)
    civ_id = models.ForeignKey('Entities', related_name='civ_identities', null=True, on_delete=models.SET_NULL)
    nemesis = models.ForeignKey('HistoricalFigures', related_name='nemesis_identities', null=True, on_delete=models.SET_NULL)
    race = models.CharField(max_length=500, null=True)
    caste = models.CharField(max_length=500, null=True)
    profession = models.CharField(max_length=500, null=True)

class EntityPositionLink(models.Model):
    world = models.ForeignKey('World', related_name='world_entity_position_link', null=True, on_delete=models.CASCADE)
    civ_id = models.ForeignKey('Entities', related_name='civ_entity_position_link', null=True, on_delete=models.SET_NULL)
    hf_id = models.ForeignKey('HistoricalFigures', related_name='hf_entity_position_link', null=True, on_delete=models.SET_NULL)
    position_id = models.ForeignKey('EntityPosition', related_name='entity_position_link', null=True, on_delete=models.SET_NULL)
    start_year = models.IntegerField(null=True)

class VagueRelationship(models.Model):
    world = models.ForeignKey('World', related_name='world_vague_relationship', null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=500)
    source_hfid = models.ForeignKey('HistoricalFigures', related_name='source_vague_relationship', null=True, on_delete=models.SET_NULL)
    target_hfid = models.ForeignKey('HistoricalFigures', related_name='target_vague_relationship', null=True, on_delete=models.SET_NULL)

class EntitySquadLink(models.Model):
    world = models.ForeignKey('World', related_name='world_entity_squad_link', null=True, on_delete=models.CASCADE)
    hf_id = models.ForeignKey('HistoricalFigures', related_name='hf_entity_squad_link', null=True, on_delete=models.SET_NULL)
    squad_id = models.IntegerField(null=True)
    squad_position = models.IntegerField(null=True)
    civ_id = models.ForeignKey('Entities', related_name='civ_entity_squad_link', null=True, on_delete=models.SET_NULL)
    start_year = models.IntegerField(null=True)

class PlotActor(models.Model):
    world = models.ForeignKey('World', related_name='world_plot_actor', null=True, on_delete=models.CASCADE)
    plot = models.ForeignKey('IntriguePlot', related_name='plot_plot_actor', null=True, on_delete=models.SET_NULL)
    actor_id = models.ForeignKey('HistoricalFigures', related_name='actor_plot_actor', null=True, on_delete=models.SET_NULL)
    plot_role = models.CharField(max_length=500, null=True)
    delegated_plot_hfid = models.ForeignKey('HistoricalFigures', related_name='delegated_plot_hfid_plot_actor', null=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=500, null=True)
    has_messenger = models.BooleanField(null=True, default=False)