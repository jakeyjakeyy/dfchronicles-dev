def save_historical_event_collection(element, world):
    from chronicle_compiler import models
    exclude_tags = ['start_seconds72', 'end_seconds72', 'ordinal', 'war_eventcol', 'eventcol', 'feature_layer_id', 'attacking_squad_entity_pop', 'defending_squad_entity_pop', 'parent_eventcol', 'individual_merc', 'attacking_merc_enid', 'company_merc']

    chronicle_id, aggressor_entity_id, attacking_squad_animated, attacking_squad_site, defender_entity_id, defending_squad_animated, defending_squad_site, civ_id, coords, end_year, name, occasion_id, outcome, site_id, start_year, subregion_id, type, attacking_squad_race, defending_squad_race, target_entity_id = None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None

    attacking_squad_number, defending_squad_number, attacking_squad_deaths, defending_squad_deaths = 0, 0, 0, 0

    attacking_hfids = []
    defending_hfids = []
    attacking_squad_races = []
    defending_squad_races = []
    events = []
    noncom_hfids = []

    for child in element:
        tag = child.tag.strip()
        if child.tag == 'id':
            chronicle_id = child.text
        elif tag == 'aggressor_ent_id':
            aggressor_entity_id = child.text
        elif tag == 'attacking_hfid' or tag == 'attacking_enid' or tag == 'attacking_merc_enid':
            attacking_hfids.append(child.text)
        elif tag == 'attacking_squad_animated':
            attacking_squad_animated = True
        elif tag == 'attacking_squad_deaths':
            attacking_squad_deaths += int(child.text)
        elif tag == 'attacking_squad_number':
            attacking_squad_number += int(child.text)
        elif tag == 'attacking_squad_race':
            if child.text not in attacking_squad_races:
                attacking_squad_races.append(child.text)
        elif tag == 'attacking_squad_site':
            attacking_squad_site = child.text
        elif tag == 'defender_ent_id' or tag == 'defending_enid':
            defender_entity_id = child.text
        elif tag == 'defending_hfid':
            defending_hfids.append(child.text)
        elif tag == 'defending_squad_animated':
            defending_squad_animated = True
        elif tag == 'defending_squad_deaths':
            defending_squad_deaths += int(child.text)
        elif tag == 'defending_squad_number':
            defending_squad_number += int(child.text)
        elif tag == 'defending_squad_race':
            if child.text not in defending_squad_races:
                defending_squad_races.append(child.text)
        elif tag == 'defending_squad_site':
            defending_squad_site = child.text
        elif tag == 'civ_id':
            civ_id = child.text
        elif tag == 'coords':
            coords = child.text
        elif tag == 'end_year':
            end_year = child.text
        elif tag == 'event':
            events.append(child.text)
        elif tag == 'name':
            name = child.text
        elif tag == 'noncom_hfid':
            noncom_hfids.append(child.text)
        elif tag == 'occasion_id':
            occasion_id = child.text
        elif tag == 'outcome':
            outcome = child.text
        elif tag == 'site_id':
            site_id = child.text
        elif tag == 'start_year':
            start_year = child.text
        elif tag == 'subregion_id':
            subregion_id = child.text
        elif tag == 'target_entity_id':
            target_entity_id = child.text
        elif tag == 'type':
            type = child.text
        elif tag in exclude_tags:
            pass
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Historical Event Collection: ' + tag + '\n')

    if len(attacking_squad_races) > 0:
        attacking_squad_race = ", ".join(attacking_squad_races)
    if len(defending_squad_races) > 0:
        defending_squad_race = ", ".join(defending_squad_races)
        
    event_collection = models.HistoricalEventCollections.objects.create(world=world, chronicle_id=chronicle_id, attacking_squad_animated=attacking_squad_animated, attacking_squad_deaths=attacking_squad_deaths, attacking_squad_number=attacking_squad_number, attacking_squad_race=attacking_squad_race, defending_squad_animated=defending_squad_animated, defending_squad_deaths=defending_squad_deaths, defending_squad_number=defending_squad_number, defending_squad_race=defending_squad_race, coords=coords, end_year=end_year, name=name, occasion_id=occasion_id, outcome=outcome, start_year=start_year, subregion_id=subregion_id, type=type)
    event_collection.save()

    missing = []
    if civ_id:
        try:
            civ = models.Entities.objects.get(world=world, chronicle_id=civ_id)
            event_collection.civ_id = civ
        except models.Entities.DoesNotExist:
            missing.append({'event_collection': event_collection, 'civ_id': civ_id})
    if site_id:
        try:
            site = models.Sites.objects.get(world=world, chronicle_id=site_id)
            event_collection.site_id = site
        except models.Sites.DoesNotExist:
            missing.append({'event_collection': event_collection, 'site_id': site_id})
    if aggressor_entity_id:
        try:
            entity = models.Entities.objects.get(world=world, chronicle_id=aggressor_entity_id)
            event_collection.aggressor_entity_id = entity
        except models.Entities.DoesNotExist:
            missing.append({'event_collection': event_collection, 'aggressor_entity_id': aggressor_entity_id})
    if defender_entity_id:
        try:
            entity = models.Entities.objects.get(world=world, chronicle_id=defender_entity_id)
            event_collection.defender_entity_id = entity
        except models.Entities.DoesNotExist:
            missing.append({'event_collection': event_collection, 'defender_entity_id': defender_entity_id})
    if attacking_squad_site:
        try:
            site = models.Sites.objects.get(world=world, chronicle_id=attacking_squad_site)
            event_collection.attacking_squad_site = site
        except models.Sites.DoesNotExist:
            missing.append({'event_collection': event_collection, 'attacking_squad_site': attacking_squad_site})
    if defending_squad_site:
        try:
            site = models.Sites.objects.get(world=world, chronicle_id=defending_squad_site)
            event_collection.defending_squad_site = site
        except models.Sites.DoesNotExist:
            missing.append({'event_collection': event_collection, 'defending_squad_site': defending_squad_site})
    if len(attacking_hfids) > 0:
        for hf_id in attacking_hfids:
            try:
                hf = models.HistoricalFigures.objects.get(world=world, chronicle_id=hf_id)
                event_collection.attacking_hfid.add(hf)
            except models.HistoricalFigures.DoesNotExist:
                missing.append({'event_collection': event_collection, 'attacking_hfid': hf_id})
    if len(defending_hfids) > 0:
        for hf_id in defending_hfids:
            try:
                hf = models.HistoricalFigures.objects.get(world=world, chronicle_id=hf_id)
                event_collection.defending_hfid.add(hf)
            except models.HistoricalFigures.DoesNotExist:
                missing.append({'event_collection': event_collection, 'defending_hfid': hf_id})
    if len(noncom_hfids) > 0:
        for hf_id in noncom_hfids:
            try:
                hf = models.HistoricalFigures.objects.get(world=world, chronicle_id=hf_id)
                event_collection.noncom_hfid.add(hf)
            except models.HistoricalFigures.DoesNotExist:
                missing.append({'event_collection': event_collection, 'noncom_hfid': hf_id})
    if len(events) > 0:
        for event in events:
            try:
                event = models.HistoricalEvents.objects.get(world=world, chronicle_id=event)
                event_collection.event.add(event)
            except models.HistoricalEvents.DoesNotExist:
                missing.append({'event_collection': event_collection, 'event': event})
    if target_entity_id:
        try:
            entity = models.Entities.objects.get(world=world, chronicle_id=target_entity_id)
            event_collection.target_entity_id = entity
        except models.Entities.DoesNotExist:
            missing.append({'event_collection': event_collection, 'target_entity_id': target_entity_id})

    event_collection.save()
    
    if missing:
        return missing
 