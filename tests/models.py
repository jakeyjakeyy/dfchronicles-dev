# Sample django models
from django.db import models


class Artifact(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    site_id = models.IntegerField()
    holder_id = models.ForeignKey('HistoricalFigure', null=True, related_name='artifacts')
    name_string = models.CharField(max_length=100)
    page_number = models.IntegerField(null=True)
    written_content_id = models.ForeignKey('WrittenContent', null=True, related_name='artifacts')
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
    entity_position = models.ManyToManyField('EntityPosition', related_name='entities')

class EntityPosition(models.Model):
    position_id = models.IntegerField()
    entity_id = models.ForeignKey('Entities', related_name='entity_position')
    name = models.CharField(max_length=100)
    name_male = models.CharField(max_length=100, null=True)
    name_female = models.CharField(max_length=100, null=True)
    spouse = models.CharField(max_length=100, null=True)
    spouse_male = models.CharField(max_length=100, null=True)
    spouse_female = models.CharField(max_length=100, null=True)

class EntityPositionAssignment(models.Model):
    position_id = models.ForeignKey('EntityPosition', related_name='entity_position_assignment')
    historical_figure_id = models.ForeignKey('HistoricalFigure', related_name='entity_position_assignment')

class EntityPopulations(models.Model):
    civ_id = models.ForeignKey('Entities', related_name='entity_populations')
    # race and pop aren't separated in the XML
    # I imagine this will be easier to split on entity creation
    race = models.CharField(max_length=100)
    population = models.IntegerField()

# I imagine this has more data, need a larger sample to confirm
class HistoricalEras(models.Model):
    name = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True)

class HistoricalEventCollections(models.Model):
    aggressor_entity_id = models.ForeignKey('Entities', related_name='historical_event_collections', null=True)
    attacking_hfid = models.ForeignKey('HistoricalFigure', related_name='historical_event_collections', null=True)
    attacking_squad_deaths = models.IntegerField(null=True)
    attacking_squad_entity_pop = models.IntegerField(null=True)
    attacking_squad_number = models.IntegerField(null=True)
    attacking_squad_race = models.CharField(max_length=100, null=True)
    attacking_squad_site = models.ForeignKey('Sites', related_name='historical_event_collections', null=True)
    defender_entity_id = models.ForeignKey('Entities', related_name='historical_event_collections', null=True)
    defending_hfid = models.ForeignKey('HistoricalFigure', related_name='historical_event_collections', null=True)
    defending_squad_deaths = models.IntegerField(null=True)
    defending_squad_entity_pop = models.IntegerField(null=True)
    defending_squad_number = models.IntegerField(null=True)
    defending_squad_race = models.CharField(max_length=100, null=True)
    defending_squad_site = models.ForeignKey('Sites', related_name='historical_event_collections', null=True)
    civ_id = models.ForeignKey('Entities', related_name='historical_event_collections')
    end_year = models.IntegerField(null=True)
    # Not sure what event is
    event = models.CharField(max_length=100)
    # Not sure what eventcol is
    eventcol = models.IntegerField(null=True)
    feature_layer_id = models.IntegerField(null=True)
    name = models.CharField(max_length=100, null=True)
    occasion_id = models.IntegerField(null=True)
    outcome = models.CharField(max_length=100, null=True)
    site_id = models.ForeignKey('Sites', related_name='historical_event_collections', null=True)
    start_year = models.IntegerField(null=True)
    subregion_id = models.IntegerField(null=True)
    type = models.CharField(max_length=100, null=True)
    # Not sure what war_eventcol is
    war_eventcol = models.IntegerField(null=True)

class HistoricalEvents(models.Model):
    