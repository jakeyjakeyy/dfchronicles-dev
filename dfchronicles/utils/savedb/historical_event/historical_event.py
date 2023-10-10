def save_historical_event(event, world):
    from chronicle_compiler import models
    chronicle_id, body_part, caste, civ_id, death_cause, hf_id, injury_type, link_type, new_job, old_job, part_lost, position, race, reason, relationship, site_id, state, subregion_id, target_hfid, type, year, coords, body_state, death_penalty, wrongful_conviction, crime, framer_hfid, fooled_hfid, convicter_enid, convicted_hfid, circumstance, stash_site, theft_method, structure = None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None

    exclude_tags = ['seconds72', 'feature_layer_id']
    for child in event:
        tag = child.tag.strip()
        if tag == 'id':
            chronicle_id = child.text
        elif tag == 'body_part':
            body_part = child.text
        elif tag == 'caste':
            caste = child.text
        elif tag == 'civ_id':
            if int(child.text) != -1:
                civ_id = child.text
        elif tag == 'death_cause':
            death_cause = child.text
        elif tag == 'histfig' or tag == 'wounder' or tag == 'hfid':
            if int(child.text) != -1:
                hf_id = child.text
        elif tag == 'injury_type':
            injury_type = child.text
        elif tag == 'link_type':
            link_type = child.text
        elif tag == 'new_job':
            new_job = child.text
        elif tag == 'old_job':
            old_job = child.text
        elif tag == 'part_lost':
            part_lost = True
        elif tag == 'position':
            position = child.text
        elif tag == 'race':
            race = child.text
        elif tag == 'reason':
            reason = child.text
        elif tag == 'relationship':
            relationship = child.text
        elif tag == 'site_id' or tag == 'site':
            if int(child.text) != -1:
                site_id = child.text
        elif tag == 'state':
            state = child.text
        elif tag == 'subregion_id':
            subregion_id = child.text
        elif tag == 'target_hfid' or tag == 'woundee' or tag == 'target':
            target_hfid = child.text
        elif tag == 'type':
            type = child.text
        elif tag == 'year':
            year = child.text
        elif tag == 'coords':
            coords = child.text
        elif tag == 'body_state':
            body_state = child.text
        elif tag == 'death_penalty':
            death_penalty = True
        elif tag == 'wrongful_conviction':
            wrongful_conviction = True
        elif tag == 'crime':
            crime = child.text
        elif tag == 'framer_hfid':
            framer_hfid = child.text
        elif tag == 'fooled_hfid':
            fooled_hfid = child.text
        elif tag == 'convicter_enid':
            convicter_enid = child.text
        elif tag == 'convicted_hfid':
            convicted_hfid = child.text
        elif tag == 'circumstance_id':
            circumstance = child.text
        elif tag == 'stash_site':
            if int(child.text) != -1:
                stash_site = child.text
        elif tag == 'theft_method':
            theft_method = child.text
        elif tag == 'structure':
            if int(child.text) != -1:
                structure = child.text
        elif tag in exclude_tags:
            pass
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Historical Event: ' + child.tag + '\n')
    
    try:
        he = models.HistoricalEvents.objects.get(chronicle_id=chronicle_id)
        if body_part:
            he.body_part = body_part
        if caste:
            he.caste = caste
        if death_cause:
            he.death_cause = death_cause
        if hf_id:
            he.hf_id = models.HistoricalFigures.objects.get(world=world, chronicle_id=hf_id)
        if injury_type:
            he.injury_type = injury_type
        if link_type:
            he.link_type = link_type
        if new_job:
            he.new_job = new_job
        if old_job:
            he.old_job = old_job
        if part_lost:
            he.part_lost = part_lost
        if position:
            he.position = position
        if race:
            he.race = race
        if subregion_id and int(subregion_id) != -1:
            he.subregion_id = subregion_id
        if stash_site:
            he.stash_site = models.Sites.objects.get(world=world, chronicle_id=stash_site)
        if theft_method:
            he.theft_method = theft_method
        if site_id:
            he.site_id = models.Sites.objects.get(world=world, chronicle_id=site_id)
        if structure:
            site_id = he.site_id
            he.structure = models.Structures.objects.get(world=world, structure_id=structure, site_id=site_id)
        
        he.save()
    except models.HistoricalEvents.DoesNotExist:
        if hf_id:
            hf_id = models.HistoricalFigures.objects.get(world=world, chronicle_id=hf_id)
        if site_id:
            site_id = models.Sites.objects.get(world=world, chronicle_id=site_id)
        if target_hfid:
            target_hfid = models.HistoricalFigures.objects.get(world=world, chronicle_id=target_hfid)
        if framer_hfid:
            framer_hfid = models.HistoricalFigures.objects.get(world=world, chronicle_id=framer_hfid)
        if fooled_hfid:
            fooled_hfid = models.HistoricalFigures.objects.get(world=world, chronicle_id=fooled_hfid)
        if convicted_hfid:
            convicted_hfid = models.HistoricalFigures.objects.get(world=world, chronicle_id=convicted_hfid)
        if convicter_enid:
            convicter_enid = models.Entities.objects.get(world=world, chronicle_id=convicter_enid)
        if stash_site:
            stash_site = models.Sites.objects.get(world=world, chronicle_id=stash_site)
        if structure:
            structure = models.Structures.objects.get(world=world, structure_id=structure, site_id=site_id)
        if civ_id:
            civ_id = models.Entities.objects.get(world=world, chronicle_id=civ_id)

        he = models.HistoricalEvents.objects.create(world=world, chronicle_id=chronicle_id, civ_id=civ_id, body_part=body_part, caste=caste, death_cause=death_cause, hf_id=hf_id, injury_type=injury_type, link_type=link_type, new_job=new_job, old_job=old_job, part_lost=part_lost, position=position, race=race, reason=reason, relationship=relationship, site_id=site_id, state=state, subregion_id=subregion_id, target_hfid=target_hfid, type=type, year=year, coords=coords, body_state=body_state, death_penalty=death_penalty, wrongful_conviction=wrongful_conviction, crime=crime, framer_hfid=framer_hfid, fooled_hfid=fooled_hfid, convicter_enid=convicter_enid, convicted_hfid=convicted_hfid, stash_site=stash_site, theft_method=theft_method, structure=structure)
        he.save()

        if circumstance:
            return {'historical_event': he, 'circumstance': circumstance}