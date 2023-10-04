from django.contrib import admin

from .models import Artifact, Entities, EntityPosition, EntityPositionAssignment, EntityPopulations, Occasion, Schedule, Feature, HistoricalEras, HistoricalEventCollections, HistoricalEvents, HistoricalEventRelationships, HistoricalFigures, EntityLink, SiteLink, HfSkill, HfLink, Regions, Sites, Structures, UndergroundRegions, WrittenContents
# Register your models here.

admin.site.register(Artifact)
admin.site.register(Entities)
admin.site.register(EntityPosition)
admin.site.register(EntityPositionAssignment)
admin.site.register(EntityPopulations)
admin.site.register(Occasion)
admin.site.register(Schedule)
admin.site.register(Feature)
admin.site.register(HistoricalEras)
admin.site.register(HistoricalEventCollections)
admin.site.register(HistoricalEvents)
admin.site.register(HistoricalEventRelationships)
admin.site.register(HistoricalFigures)
admin.site.register(EntityLink)
admin.site.register(SiteLink)
admin.site.register(HfSkill)
admin.site.register(HfLink)
admin.site.register(Regions)
admin.site.register(Sites)
admin.site.register(Structures)
admin.site.register(UndergroundRegions)
admin.site.register(WrittenContents)