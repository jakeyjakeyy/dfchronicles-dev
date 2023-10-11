def save_historical_event(event, world):
    from chronicle_compiler import models
    chronicle_id, body_part, caste, death_cause, hf_id, injury_type, link_type, new_job, old_job, part_lost, position, race, reason, relationship, state, subregion_id, target_hfid, type, year, coords, body_state, death_penalty, wrongful_conviction, crime, framer_hfid, fooled_hfid, convicter_enid, convicted_hfid, circumstance, stash_site, theft_method, structure, knowledge, first, link, position_id, site_civ_id, target_enid, artifact, identity, occasion, schedule, attacker_civ_id, defender_civ_id, attacker_general_hfid, defender_general_hfid, subtype, initiating_entity, dispute, winner_hfid = None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None

    civ_ids = []
    site_ids = []
    joining_entities = []
    competitor_hfids = []

    missing_fkeys = []
    exclude_tags = ['seconds72', 'feature_layer_id', 'unit_id', 'agreement_id', 'slayer_race', 'slayer_caste', 'slayer_item_id', 'slayer_shooter_item_id']
    for child in event:
        tag = child.tag.strip()
        if tag == 'id':
            chronicle_id = child.text
        elif tag == 'body_part':
            body_part = child.text
        elif tag == 'caste':
            caste = child.text
        elif tag == 'civ_id' or tag == 'entity_id_1' or tag == 'entity_id_2' or tag == 'entity_id':
            if int(child.text) != -1:
                civ_ids.append(child.text)
        elif tag == 'death_cause' or tag == 'cause':
            death_cause = child.text
        elif tag == 'histfig' or tag == 'wounder' or tag == 'hfid' or tag == 'builder_hfid' or tag == 'trickster_hfid' or tag == 'hist_figure_id' or tag == 'slayer_hfid' or tag == 'group_1_hfid':
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
        elif tag == 'site_id' or tag == 'site' or tag == 'site_id_1' or tag == 'site_id_2':
            if int(child.text) != -1:
                site_ids.append(child.text)
        elif tag == 'state':
            state = child.text
        elif tag == 'subregion_id':
            subregion_id = child.text
        elif tag == 'target_hfid' or tag == 'woundee' or tag == 'target' or tag == 'group_2_hfid' or tag == 'hfid_target':
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
        elif tag == 'structure' or tag == 'structure_id':
            if int(child.text) != -1:
                structure = child.text
        elif tag == 'knowledge':
            knowledge = child.text
        elif tag == 'first':
            first = True
        elif tag == 'link':
            link = child.text
        elif tag == 'position_id':
            position_id = child.text
        elif tag == 'site_civ_id':
            if int(child.text) != -1:
                site_civ_id = child.text
        elif tag == 'target_enid':
            if int(child.text) != -1:
                target_enid = child.text
        elif tag == 'artifact_id':
            if int(child.text) != -1:
                artifact = child.text
        elif tag == 'identity_id':
            identity = child.text
        elif tag == 'occasion_id':
            occasion = child.text
        elif tag == 'schedule_id':
            schedule = child.text
        elif tag == 'attacker_civ_id':
            if int(child.text) != -1:
                attacker_civ_id = child.text
        elif tag == 'defender_civ_id':
            if int(child.text) != -1:
                defender_civ_id = child.text
        elif tag == 'attacker_general_hfid':
            if int(child.text) != -1:
                attacker_general_hfid = child.text
        elif tag == 'defender_general_hfid':
            if int(child.text) != -1:
                defender_general_hfid = child.text
        elif tag == 'subtype':
            subtype = child.text
        elif tag == 'initiating_enid':
            initiating_entity = child.text
        elif tag == 'joining_enid':
            joining_entities.append(child.text)
        elif tag == 'dispute':
            dispute = child.text
        elif tag == 'winner_hfid':
            winner_hfid = models.HistoricalFigures.objects.get(world=world, chronicle_id=child.text)
        elif tag == 'competitor_hfid':
            competitor_hfids.append(child.text)
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
        if site_ids:
            for site_id in site_ids:
                he.site_id.add(models.Sites.objects.get(world=world, chronicle_id=site_id))
        if structure:
            site_id = models.Sites.objects.get(world=world, chronicle_id=site_ids[0])
            he.structure = models.Structures.objects.get(world=world, structure_id=structure, site_id=site_id)
        
        he.save()
    except models.HistoricalEvents.DoesNotExist:
        if hf_id:
            hf_id = models.HistoricalFigures.objects.get(world=world, chronicle_id=hf_id)
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
            structure = models.Structures.objects.get(world=world, structure_id=structure, site_id=models.Sites.objects.get(world=world, chronicle_id=site_ids[0]))
        if target_enid:
            target_enid = models.Entities.objects.get(world=world, chronicle_id=target_enid)
        if artifact:
            artifact = models.Artifact.objects.get(world=world, chronicle_id=artifact)
        if attacker_civ_id:
            attacker_civ_id = models.Entities.objects.get(world=world, chronicle_id=attacker_civ_id)
        if defender_civ_id:
            defender_civ_id = models.Entities.objects.get(world=world, chronicle_id=defender_civ_id)
        if attacker_general_hfid:
            attacker_general_hfid = models.HistoricalFigures.objects.get(world=world, chronicle_id=attacker_general_hfid)
        if defender_general_hfid:
            defender_general_hfid = models.HistoricalFigures.objects.get(world=world, chronicle_id=defender_general_hfid)
        if site_civ_id:
            site_civ_id = models.Entities.objects.get(world=world, chronicle_id=site_civ_id)
        if initiating_entity:
            initiating_entity = models.Entities.objects.get(world=world, chronicle_id=initiating_entity)
        

        he = models.HistoricalEvents.objects.create(world=world, chronicle_id=chronicle_id, body_part=body_part, caste=caste, death_cause=death_cause, hf_id=hf_id, injury_type=injury_type, link_type=link_type, new_job=new_job, old_job=old_job, part_lost=part_lost, position=position, race=race, reason=reason, relationship=relationship, state=state, subregion_id=subregion_id, target_hfid=target_hfid, type=type, year=year, coords=coords, body_state=body_state, death_penalty=death_penalty, wrongful_conviction=wrongful_conviction, crime=crime, framer_hfid=framer_hfid, fooled_hfid=fooled_hfid, convicter_enid=convicter_enid, convicted_hfid=convicted_hfid, stash_site=stash_site, theft_method=theft_method, structure=structure, knowledge=knowledge, first=first, link=link, site_civ_id=site_civ_id, target_enid=target_enid, artifact=artifact, attacker_civ_id=attacker_civ_id, defender_civ_id=defender_civ_id, attacker_general_hfid=attacker_general_hfid, defender_general_hfid=defender_general_hfid, subtype=subtype, initiating_entity=initiating_entity, dispute=dispute, winner_hfid=winner_hfid)
        he.save()

        if civ_ids:
            for civ_id in civ_ids:
                he.civ_id.add(models.Entities.objects.get(world=world, chronicle_id=civ_id))
        if site_ids:
            for site_id in site_ids:
                he.site_id.add(models.Sites.objects.get(world=world, chronicle_id=site_id))
        if joining_entities:
            for joining_entity in joining_entities:
                he.joining_entity.add(models.Entities.objects.get(world=world, chronicle_id=joining_entity))
        if competitor_hfids:
            for competitor_hfid in competitor_hfids:
                he.competitor_hfid.add(models.HistoricalFigures.objects.get(world=world, chronicle_id=competitor_hfid))

        he.save()
        

        if circumstance:
            missing_fkeys.append({'historical_event': he, 'circumstance_id': circumstance})
        if position_id:
            missing_fkeys.append({'historical_event': he, 'position_id': position_id})
        if identity:
            missing_fkeys.append({'historical_event': he, 'identity': identity})
        if occasion:
            missing_fkeys.append({'historical_event': he, 'occasion': occasion, 'civ_id': models.Entities.objects.get(world=world, chronicle_id=civ_ids[0])})
        if schedule:
            missing_fkeys.append({'historical_event': he, 'schedule': schedule, 'civ_id': models.Entities.objects.get(world=world, chronicle_id=civ_ids[0])})

        if missing_fkeys:
            return missing_fkeys