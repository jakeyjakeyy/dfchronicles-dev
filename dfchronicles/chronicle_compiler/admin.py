from django.contrib import admin

from .models import World, Artifact, Entities, EntityPosition, EntityPositionAssignment, EntityPopulations, Occasion, Schedule, Feature, HistoricalEras, HistoricalEventCollections, HistoricalEvents, HistoricalFigures, EntityLink, SiteLink, HfSkill, HfLink, Regions, Sites, Structures, UndergroundRegions, WrittenContents, IntriguePlot, IntrigueActor, RelationshipProfileVisual, EntityFormerPositionLink, Identities, EntityPositionLink, VagueRelationship, EntitySquadLink, PlotActor, SiteProperty
# Register your models here.


class EntityPositionInline(admin.TabularInline):
    model = EntityPosition
    extra = 0
class OccasionInline(admin.TabularInline):
    model = Occasion
    extra = 0
    
class EntitiesAdmin(admin.ModelAdmin):
    inlines = [
        EntityPositionInline, OccasionInline
    ]

admin.site.register(World)
admin.site.register(Artifact)
admin.site.register(Entities, EntitiesAdmin)
admin.site.register(EntityPosition)
admin.site.register(EntityPositionAssignment)
admin.site.register(EntityPopulations)
admin.site.register(Occasion)
admin.site.register(Schedule)
admin.site.register(Feature)
admin.site.register(HistoricalEras)
admin.site.register(HistoricalEventCollections)
admin.site.register(HistoricalEvents)
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
admin.site.register(IntrigueActor)
admin.site.register(RelationshipProfileVisual)
admin.site.register(EntityFormerPositionLink)
admin.site.register(Identities)
admin.site.register(EntityPositionLink)
admin.site.register(VagueRelationship)
admin.site.register(EntitySquadLink)
admin.site.register(PlotActor)
admin.site.register(IntriguePlot)
admin.site.register(SiteProperty)