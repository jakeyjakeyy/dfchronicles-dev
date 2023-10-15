from .circumstance import save_circumstance

def save_historical_event(event, world):
    from chronicle_compiler import models
    chronicle_id, body_part, caste, death_cause, hf_id, injury_type, link_type, new_job, old_job, part_lost, position, race, reason, relationship, state, subregion_id, target_hfid, type, year, coords, body_state, death_penalty, wrongful_conviction, crime, framer_hfid, fooled_hfid, convicter_enid, convicted_hfid, circumstance, stash_site, theft_method, structure, knowledge, first, link, position_id, site_civ_id, target_enid, artifact, occasion, schedule, attacker_civ_id, defender_civ_id, attacker_general_hfid, defender_general_hfid, subtype, initiating_entity, dispute, winner_hfid, detected, written_content, returning, old_race, old_caste, new_race, new_caste, quality, old_account, new_account, identity, target_identity, identity_rep, target_identity_rep, secret_goal, method, world_construction, master_world_construction, site_property, last_owner, rebuilt_ruined, inherited, purchased_unowned, corruptor_seen_as, target_seen_as, successful, mood, new_site_civ, new_leader, prison_months, target_site, account_shift, shrine_amount_destroyed, resident_civ_id, position_taker_hfid, instigator_hfid, actor_hfid, feature_layer_id, musical_form, poetic_form, dance_form, held_firm_in_interrogation, pets, mat, abuse_type, circumstance_id = None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None

    civ_ids = []
    site_ids = []
    joining_entities = []
    competitor_hfids = []
    expelled_hfids = []
    conspirator_hfids = []
    bodies = []

    missing_fkeys = []
    exclude_tags = ['seconds72', 'unit_id', 'agreement_id', 'slayer_race', 'slayer_caste', 'slayer_item_id', 'slayer_shooter_item_id', 'name_only', 'position_profile_id', 'interaction', 'top_value', 'top_value_rating', 'top_value_modifier', 'ally_defense_bonus', 'top_facet', 'top_facet_rating', 'top_facet_modifier', 'failed_judgment_test', 'top_relationship_factor', 'top_relationship_rating', 'top_relationship_modifier', 'relevant_entity_id', 'relevant_position_profile_id', 'allotment', 'allotment_index', 'expelled_creature', 'expelled_pop_id', 'expelled_number', 'production_zone_id', 'surveiled_convicted', 'lure_hfid', 'coconspirator_bonus', 'pop_race', 'pop_number_moved', 'pop_srid', 'pop_flid', 'relevant_id_for_method', 'law_add', 'law_remove', 'delegated', 'woundee_race', 'woundee_caste', 'attacker_merc_enid', 'religion_id', 'appointer_hfid', 'promise_to_hfid', 'identity_name', 'creator_unit_id', 'mattype', 'matindex', 'identity_nemesis_id', 'identity_race', 'identity_caste', 'item', 'unk_1', 'tree', 'pile_type']
    for child in event:
        tag = child.tag.strip()
        if tag == 'id':
            chronicle_id = child.text
        elif tag == 'body_part':
            body_part = child.text
        elif tag == 'caste':
            caste = child.text
        elif tag in ['civ_id', 'entity_id_1', 'entity_id_2', 'entity_id', 'giver_entity_id', 'trader_entity_id', 'persecutor_enid', 'entity_1', 'entity_2', 'civ_entity_id', 'civ', 'source', 'entity']:
            if int(child.text) != -1:
                civ_ids.append(child.text)
        elif tag == 'death_cause' or tag == 'cause':
            death_cause = child.text
        elif tag in ['histfig', 'wounder_hfid', 'hfid', 'builder_hfid', 'trickster_hfid', 'hist_figure_id', 'slayer_hfid', 'group_1_hfid', 'group_hfid', 'snatcher_hfid', 'changer_hfid', 'gambler_hfid', 'hfid1', 'attacker_hfid', 'teacher_hfid', 'corruptor_hfid', 'aquirer_hfid', 'seeker_hfid', 'giver_hist_figure_id', 'acquirer_hfid', 'trader_hfid', 'persecutor_hfid', 'eater', 'speaker_hfid', 'hist_fig_id', 'overthrown_hfid', 'doer_hfid', 'group', 'slayer_hf', 'wounder', 'builder_hf', 'trickster', 'creator_hfid', 'hf', 'changer', 'teacher', 'doer', 'region']:
            # prevent these from overwriting each other
            if child.tag == 'slayer_hfid' and int(child.text) != -1:
                target_hfid = hf_id
                hf_id = child.text
            elif int(child.text) != -1:
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
        elif tag in ['site_id', 'site', 'site_id1', 'site_id2', 'site_id_1', 'site_id_2', 'source_site_id', 'site_hfid']:
            if int(child.text) != -1:
                site_ids.append(child.text)
        elif tag == 'state':
            state = child.text
        elif tag == 'subregion_id':
            subregion_id = child.text
        elif tag in ['target_hfid', 'woundee_hfid', 'target', 'group_2_hfid', 'hfid_target', 'changee_hfid', 'hfid2', 'student_hfid', 'receiver_hist_figure_id', 'victim_hf', 'woundee', 'hf_target', 'changee', 'victim', 'student']:
            if int(child.text) != -1:
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
        elif tag == 'circumstance':
            circumstance = child
        elif tag == 'circumstance_id':
            circumstance_id = child.text
        elif tag == 'stash_site':
            if int(child.text) != -1:
                stash_site = child.text
        elif tag == 'theft_method':
            theft_method = child.text
        elif tag in ['structure_id', 'structure']:
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
        elif tag in ['site_civ_id', 'site_entity_id', 'site_civ']:
            if int(child.text) != -1:
                site_civ_id = child.text
        elif tag in ['target_enid', 'receiver_entity_id', 'join_entity_id', 'destination', 'victim_entity']:
            if int(child.text) != -1:
                target_enid = child.text
        elif tag in ['artifact_id', 'artifact']:
            if int(child.text) != -1:
                artifact = child.text
        elif tag in ['identity_id', 'identity_id1', 'corruptor_identity', 'identity_histfig_id']:
            identity = child.text
        elif tag == 'identity_id2':
            target_identity = child.text
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
        elif tag in ['subtype', 'action', 'claim', 'unit_type', 'topic', 'situation', 'item_type', 'item_subtype', 'secret_text', 'interaction_action']:
            try:
                if int(child.text) != -1:
                    subtype = child.text
            except:
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
        elif tag == 'detected':
            detected = True
        elif tag == 'written_content' or tag == 'wc_id':
            written_content = child.text
        elif tag == 'return':
            returning = True
        elif tag == 'old_race':
            old_race = child.text
        elif tag == 'new_race':
            new_race = child.text
        elif tag == 'old_caste':
            old_caste = child.text
        elif tag == 'new_caste':
            new_caste = child.text
        elif tag == 'hf_rep_1_of_2':
            identity_rep = child.text
        elif tag == 'hf_rep_2_of_1':
            target_identity_rep = child.text
        elif tag == 'reason_id':
            if reason == 'glorify_hf':
                target_hfid = models.HistoricalFigures.objects.get(world=world, chronicle_id=child.text)
        elif tag == 'quality':
            quality = child.text
        elif tag == 'old_account':
            old_account = child.text
        elif tag == 'new_account':
            new_account = child.text
        elif tag == 'secret_goal':
            secret_goal = child.text
        elif tag == 'method':
            method = child.text
        elif tag == 'wcid':
            world_construction = child.text
        elif tag == 'master_wcid':
            master_world_construction = child.text
        elif tag == 'building_profile_id':
            site_property = models.SiteProperty.objects.get(world=world, local_id=child.text, site_id=models.Sites.objects.get(world=world, chronicle_id=site_ids[0]))
        elif tag == 'last_owner_hfid':
            last_owner = models.HistoricalFigures.objects.get(world=world, chronicle_id=child.text)
        elif tag == 'rebuilt_ruined' or tag == 'rebuild':
            rebuilt_ruined = True
            if child.text == 'false':
                rebuilt_ruined = False
        elif tag == 'inherited':
            inherited = True
        elif tag == 'purchased_unowned':
            purchased_unowned = True
        elif tag == 'corruptor_seen_as':
            corruptor_seen_as = child.text
        elif tag == 'target_seen_as':
            target_seen_as = child.text
        elif tag == 'successful':
            successful = True
        elif tag == 'mood':
            mood = child.text
        elif tag == 'new_site_civ_id':
            new_site_civ = models.Entities.objects.get(world=world, chronicle_id=child.text)
        elif tag == 'new_leader_hfid':
            new_leader = models.HistoricalFigures.objects.get(world=world, chronicle_id=child.text)
        elif tag == 'prison_months':
            prison_months = child.text
        elif tag == 'dest_site_id':
            target_site = models.Sites.objects.get(world=world, chronicle_id=child.text)
        elif tag == 'account_shift':
            account_shift = child.text
        elif tag == 'expelled_hfid':
            expelled_hfids.append(child.text)
        elif tag == 'shrine_amount_destroyed':
            shrine_amount_destroyed = child.text
        elif tag == 'resident_civ_id':
            if int(child.text) != -1:
                resident_civ_id = models.Entities.objects.get(world=world, chronicle_id=child.text)
        elif tag == 'pos_taker_hfid':
            position_taker_hfid = models.HistoricalFigures.objects.get(world=world, chronicle_id=child.text)
        elif tag == 'instigator_hfid':
            instigator_hfid = models.HistoricalFigures.objects.get(world=world, chronicle_id=child.text)
        elif tag == 'conspirator_hfid' or tag == 'implicated_hfid':
            conspirator_hfids.append(child.text)
        elif tag == 'actor_hfid':
            actor_hfid = models.HistoricalFigures.objects.get(world=world, chronicle_id=child.text)
        elif tag == 'feature_layer_id':
            if int(child.text) != -1:
                feature_layer_id = child.text
        elif tag == 'form_id':
            if type == 'musical form created':
                musical_form = child.text
            elif type == 'poetic form created':
                poetic_form = child.text
            elif type == 'dance form created':
                dance_form = child.text
        elif tag == 'held_firm_in_interrogation':
            held_firm_in_interrogation = True
        elif tag == 'pets':
            pets = child.text
        elif tag in ['mat', 'item_mat']:
            mat = child.text
        elif tag == 'bodies':
            bodies.append(child.text)
        elif tag == 'abuse_type':
            abuse_type = child.text
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
        if mat:
            he.mat = mat
        if civ_ids:
            for civ_id in civ_ids:
                he.civ_id.add(models.Entities.objects.get(world=world, chronicle_id=civ_id))
        if target_hfid:
            he.target_hfid = models.HistoricalFigures.objects.get(world=world, chronicle_id=target_hfid)
        if structure:
            site_id = models.Sites.objects.get(world=world, chronicle_id=site_ids[0])
            he.structure = models.Structures.objects.get(world=world, structure_id=structure, site_id=site_id)
        if subtype:
            he.subtype = subtype
        if bodies:
            for body in bodies:
                he.bodies.add(models.HistoricalFigures.objects.get(world=world, chronicle_id=body))
        if target_enid:
            he.target_enid = models.Entities.objects.get(world=world, chronicle_id=target_enid)
        if abuse_type:
            he.abuse_type = abuse_type
        if artifact:
            he.artifact = models.Artifact.objects.get(world=world, chronicle_id=artifact)
        

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

        he = models.HistoricalEvents.objects.create(world=world, chronicle_id=chronicle_id, body_part=body_part, caste=caste, death_cause=death_cause, hf_id=hf_id, injury_type=injury_type, link_type=link_type, new_job=new_job, old_job=old_job, part_lost=part_lost, position=position, race=race, reason=reason, relationship=relationship, state=state, subregion_id=subregion_id, target_hfid=target_hfid, type=type, year=year, coords=coords, body_state=body_state, death_penalty=death_penalty, wrongful_conviction=wrongful_conviction, crime=crime, framer_hfid=framer_hfid, fooled_hfid=fooled_hfid, convicter_enid=convicter_enid, convicted_hfid=convicted_hfid, stash_site=stash_site, theft_method=theft_method, structure=structure, knowledge=knowledge, first=first, link=link, site_civ_id=site_civ_id, target_enid=target_enid, artifact=artifact, attacker_civ_id=attacker_civ_id, defender_civ_id=defender_civ_id, attacker_general_hfid=attacker_general_hfid, defender_general_hfid=defender_general_hfid, subtype=subtype, initiating_entity=initiating_entity, dispute=dispute, winner_hfid=winner_hfid, detected=detected, returning=returning, old_race=old_race, new_race=new_race, old_caste=old_caste, new_caste=new_caste, quality=quality, old_account=old_account, new_account=new_account, identity_rep=identity_rep, target_identity_rep=target_identity_rep, secret_goal=secret_goal, method=method, site_property=site_property, last_owner=last_owner, rebuilt_ruined=rebuilt_ruined, inherited=inherited, purchased_unowned=purchased_unowned, corruptor_seen_as=corruptor_seen_as, target_seen_as=target_seen_as, successful=successful, mood=mood, new_site_civ=new_site_civ, new_leader=new_leader, prison_months=prison_months, target_site=target_site, account_shift=account_shift, shrine_amount_destroyed=shrine_amount_destroyed, resident_civ_id=resident_civ_id, position_taker_hfid=position_taker_hfid, instigator_hfid=instigator_hfid, actor_hfid=actor_hfid, held_firm_in_interrogation=held_firm_in_interrogation, pets=pets, mat=mat)
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
        if expelled_hfids:
            for expelled in expelled_hfids:
                he.expelled_hfids.add(models.HistoricalFigures.objects.get(world=world, chronicle_id=expelled))
        if conspirator_hfids:
            for conspirator in conspirator_hfids:
                he.conspirator_hfid.add(models.HistoricalFigures.objects.get(world=world, chronicle_id=conspirator))
        

        if position_id:
            try:
                he.position_id = models.EntityPosition.objects.get(world=world, civ_position_id=position_id, civ_id=models.Entities.objects.get(world=world, chronicle_id=civ_ids[0]))
            except models.EntityPosition.DoesNotExist:
                missing_fkeys.append({'historical_event': he, 'position_id': position_id})
        if identity:
            missing_fkeys.append({'historical_event': he, 'identity': identity})
        if target_identity:
            missing_fkeys.append({'historical_event': he, 'target_identity': target_identity})
        if occasion:
            try:
                occasion = models.Occasion.objects.get(world=world, civ_occasion_id=occasion, civ_id=models.Entities.objects.get(world=world, chronicle_id=civ_ids[0]))
                he.occasion = occasion
            except models.Occasion.DoesNotExist:
                missing_fkeys.append({'historical_event': he, 'occasion': occasion, 'civ_id': models.Entities.objects.get(world=world, chronicle_id=civ_ids[0])})
        if schedule:
            try:
                he.schedule = models.Schedule.objects.get(world=world, occasion_schedule_id=schedule, occasion=occasion)
            except models.Schedule.DoesNotExist:
                missing_fkeys.append({'historical_event': he, 'schedule': schedule, 'civ_id': models.Entities.objects.get(world=world, chronicle_id=civ_ids[0])})
        if written_content:
            try:
                he.written_content = models.WrittenContents.objects.get(world=world, chronicle_id=written_content)
            except models.WrittenContents.DoesNotExist:
                missing_fkeys.append({'historical_event': he, 'written_content': written_content})
        if musical_form:
            try:
                he.musical_form = models.MusicalForms.objects.get(world=world, chronicle_id=musical_form)
            except models.MusicalForms.DoesNotExist:
                missing_fkeys.append({'historical_event': he, 'musical_form': musical_form})
        if poetic_form:
            try:
                he.poetic_form = models.PoeticForms.objects.get(world=world, chronicle_id=poetic_form)
            except models.PoeticForms.DoesNotExist:
                missing_fkeys.append({'historical_event': he, 'poetic_form': poetic_form})
        if dance_form:
            try:
                he.dance_form = models.DanceForms.objects.get(world=world, chronicle_id=dance_form)
            except models.DanceForms.DoesNotExist:
                missing_fkeys.append({'historical_event': he, 'dance_form': dance_form})
        if world_construction:
            try:
                he.world_construction = models.WorldConstruction.objects.get(world=world, chronicle_id=world_construction)
            except models.WorldConstruction.DoesNotExist:
                missing_fkeys.append({'historical_event': he, 'world_construction': world_construction})
        if master_world_construction:
            try:
                he.master_world_construction = models.WorldConstruction.objects.get(world=world, chronicle_id=master_world_construction)
            except models.WorldConstruction.DoesNotExist:
                missing_fkeys.append({'historical_event': he, 'master_world_construction': master_world_construction})
        # Feature layer should be saved by this point in final build, this is temp to avoid error
        if feature_layer_id:
            try:
                he.feature_layer_id = models.UndergroundRegions.objects.get(world=world, chronicle_id=feature_layer_id)
            except models.UndergroundRegions.DoesNotExist:
                missing_fkeys.append({'historical_event': he, 'feature_layer_id': feature_layer_id})
        if circumstance:
            lists = save_circumstance(world, circumstance, he, circumstance_id)
            if lists:
                missing_fkeys.append(lists)

        he.save()

        if missing_fkeys:
            return missing_fkeys