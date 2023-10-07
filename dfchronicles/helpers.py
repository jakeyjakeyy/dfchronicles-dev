import xml.etree.ElementTree as ET
from chronicle_compiler import models


def ParseXML(root):
    exclude_tags = ['start_seconds72', 'end_seconds72', 'birth_seconds72', 'death_seconds72', 'author_roll', 'form_id', 'coords', 'rectangle', 'world_constructions']
    exclude_redundant = ['artifact', 'entity', 'entity_population', 'historical_era', 'historical_event_collection', 'historical_event', 'historical_figure', 'region', 'site', 'underground_region', 'written_content']
    def parse_element(element):
        data = {}
        for child in element:
            if child.tag not in exclude_tags:
                if len(child) > 0:
                    if child.tag not in data:
                        data[child.tag] = []
                    data[child.tag].append(parse_element(child))
                else:
                    text = child.text
                    data[child.tag] = text
        return data

    return {root.tag: parse_element(root)}

def SaveWorld(root, owner):
    owner = models.User.objects.get(id=1)
    if root[1].tag == 'altname':
        world = models.World.objects.create(name=root[1].text, name2=root[0].text, owner=owner)
        world.save()
    return world

def SaveLegends(root, world):
    class_tags = ['artifacts', 'entities', 'entity_populations', 'historical_eras', 'historical_event_collections', 'historical_events', 'historical_figures', 'regions', 'sites', 'underground_regions', 'written_contents', 'world_constructions']
    exclude_tags = ['start_seconds72', 'end_seconds72', 'birth_seconds72', 'death_seconds72', 'author_roll', 'form_id', 'coords', 'rectangle', 'world_constructions']
    missing_fkeys = []

    test_tags = ['artifacts', 'entities', 'entity_populations', 'historical_eras', 'historical_event_collections']

    # Find all elements and run associated save function
    def save_element(element, world):
        # select historic figures tag from element
        hf = element.find('historical_figures')
        if hf:
            open('log.txt', 'a').write('Saving Historical Figures...\n')
            for child in hf:
                lists = save_historical_figure(child, world)
                if lists:
                    for dict in lists:
                        missing_fkeys.append(dict)
        for child in element:
            if child.tag not in exclude_tags and child.tag in test_tags:
                open('log.txt', 'a').write('Saving ' + child.tag + '...\n')
                save_element(child, world)
            else:
                if child.tag == 'artifact':
                    lists = save_artifact(child, world)
                    if lists:
                        missing_fkeys.append(lists)
                elif child.tag == 'entity':
                    lists = save_entity(child, world)
                    if lists:
                        for dict in lists:
                            missing_fkeys.append(dict)
                elif child.tag == 'entity_population':
                    lists = save_entity_population(child, world)
                    if lists:
                        missing_fkeys.append(lists)
                elif child.tag == 'historical_era':
                    save_historical_era(child, world)
                elif child.tag == 'historical_event_collection':
                    lists = save_historical_event_collection(child, world)
                    if lists:
                        for dict in lists:
                            missing_fkeys.append(dict)
                else:
                    open('log.txt', 'a').write('!UNUSED CHILD! Save Legends: ' + child.tag + '\n')
    
    save_element(root, world)
    # open('log.txt', 'a').write('Missing Foreign Keys: ' + str(missing_fkeys) + '\n')


    
# Save functions

def save_historical_figure(element, world):
    exclude_tags = ['birth_seconds72', 'death_seconds72', 'interaction_knowledge', 'sex', 'active_interaction', 'relationship_profile_hf_historical', 'entity_reputation']
    chronicle_id, appeared, associated_type, birth_year, caste, death_year, deity, goal, name, race, journey_pet, ent_pop_id, current_identity, force, animated, animated_string = None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None

    used_identities = []
    held_artifacts = []
    spheres = []
    entity_links = []
    site_links = []
    hf_skills = []
    hf_links = []
    former_positions = []
    relationship_visuals = []
    intrigue_plots = []
    intrigue_actors = []
    entity_positions_link = []
    vague_relationships = []
    squad_links = []
    missing_fkeys = []
    for child in element:
        tag = child.tag.strip()
        if tag == 'id':
            chronicle_id = child.text
        elif tag == 'appeared':
            appeared = child.text
        elif tag == 'associated_type':
            associated_type = child.text
        elif tag == 'birth_year':
            birth_year = child.text
        elif tag == 'caste':
            caste = child.text
        elif tag == 'death_year':
            if int(child.text) == -1:
                death_year = None
            else:
                death_year = child.text
        elif tag == 'deity':
            deity = True
        elif tag == 'goal':
            goal = child.text
        elif tag == 'name':
            name = child.text
        elif tag == 'race':
            race = child.text
        elif tag == 'used_identity_id':
            used_identities.append(child.text)
        elif tag == 'sphere':
            spheres.append(child.text)
        elif tag == 'journey_pet':
            journey_pet = child.text
        elif tag == 'ent_pop_id':
            ent_pop_id = child.text
        elif tag == 'current_identity_id':
            current_identity = child.text
        elif tag == 'holds_artifact':
            held_artifacts.append(child.text)
        elif tag == 'force':
            force = child.text
        elif tag == 'animated':
            animated = True
        elif tag == 'animated_string':
            animated_string = child.text
        elif tag == 'entity_link':
            entity_links.append(child)
        elif tag == 'site_link':
            site_links.append(child)
        elif tag == 'hf_skill':
            hf_skills.append(child)
        elif tag == 'hf_link':
            hf_links.append(child)
        elif tag == 'entity_former_position_link':
            former_positions.append(child)
        elif tag == 'relationship_profile_hf_visual':
            relationship_visuals.append(child)
        elif tag == 'intrigue_plot':
            intrigue_plots.append(child)
        elif tag == 'intrigue_actor':
            intrigue_actors.append(child)
        elif tag == 'entity_position_link':
            entity_positions_link.append(child)
        elif tag == 'vague_relationship':
            vague_relationships.append(child)
        elif tag == 'entity_squad_link':
            squad_links.append(child)
        elif tag == 'entity_squad_link':
            # class EntitySquadLink
            pass
        elif tag == 'honor_entity':
            # class HonorEntity
            pass
        elif tag in exclude_tags:
            pass
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Historical Figure: ' + tag + '\n')
    
    try:
        hf = models.HistoricalFigures.objects.get(world=world, chronicle_id=chronicle_id)
        exists = True
    except models.HistoricalFigures.DoesNotExist:
        exists = False

    if exists:
        hf.race = race
        hf.save()
    else:
        sphere = None
        if len(spheres) > 0:
            sphere = ", ".join(spheres)
      
        hf = models.HistoricalFigures.objects.create(world=world, chronicle_id=chronicle_id, appeared=appeared, associated_type=associated_type, birth_year=birth_year, caste=caste, death_year=death_year, deity=deity, goal=goal, name=name, race=race, sphere=sphere, journey_pet=journey_pet, force=force, animated=animated, animated_string=animated_string)
        hf.save()

    if len(entity_links) > 0:
        for link in entity_links:
            lists = save_entity_link(link, hf)
            if lists:
                for dict in lists:
                    missing_fkeys.append(dict)
    if len(site_links) > 0:
        for link in site_links:
            lists = save_site_link(link, hf)
            if lists:
                for dict in lists:
                    missing_fkeys.append(dict)
    if len(hf_skills) > 0:
        for skill in hf_skills:
            lists = save_hf_skill(skill, hf)
            if lists:
                for dict in lists:
                    missing_fkeys.append(dict)
    if len(hf_links) > 0:
        for link in hf_links:
            links = save_hf_link(link, hf)
            if links:
                for dict in links:
                    missing_fkeys.append(dict)
    if len(former_positions) > 0:
        for position in former_positions:
            links = save_entity_former_position_link(position, hf)
            if links:
                for dict in links:
                    missing_fkeys.append(dict)
    if len(relationship_visuals) > 0:
        for visual in relationship_visuals:
            links = save_relationship_profile_visual(visual, hf)
            if links:
                for dict in links:
                    missing_fkeys.append(dict)
    if len(intrigue_plots) > 0:
        for plot in intrigue_plots:
            links = save_intrigue_plot(plot, hf)
            if links:
                for dict in links:
                    missing_fkeys.append(dict)
    if len(intrigue_actors) > 0:
        for actor in intrigue_actors:
            links = save_intrigue_actor(actor, hf)
            if links:
                for dict in links:
                    missing_fkeys.append(dict)
    if len(entity_positions_link) > 0:
        for position in entity_positions_link:
            links = save_entity_position_link(position, hf)
            if links:
                for dict in links:
                    missing_fkeys.append(dict)
    if len(vague_relationships) > 0:
        for relationship in vague_relationships:
            links = save_vague_relationship(relationship, hf)
            if links:
                for dict in links:
                    missing_fkeys.append(dict)
    if len(squad_links) > 0:
        for squad in squad_links:
            links = save_entity_squad_link(squad, hf)
            if links:
                for dict in links:
                    missing_fkeys.append(dict)

    if current_identity:
        missing_fkeys.append({'historicfigure': hf, 'current_identity': current_identity})
    if len(used_identities) > 0:
        for identity in used_identities:
            missing_fkeys.append({'historicfigure': hf, 'used_identity': identity})
    if len(held_artifacts) > 0:
        for artifact in held_artifacts:
            missing_fkeys.append({'historicfigure': hf, 'held_artifact': artifact})
    if ent_pop_id:
        missing_fkeys.append({'historicfigure': hf, 'ent_pop_id': ent_pop_id})
    
    if missing_fkeys:
        return missing_fkeys
    
def save_entity_link(element, hf):
    civ_id, link_type, link_strength = None, None, None
    for child in element:
        tag = child.tag.strip()
        if tag == 'entity_id':
            civ_id = child.text
        elif tag == 'link_type':
            link_type = child.text
        elif tag == 'link_strength':
            link_strength = child.text
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Entity Link: ' + tag + '\n')
    
    entity_link = models.EntityLink.objects.create(world=hf.world, hf_id=hf, link_type=link_type, link_strength=link_strength)
    entity_link.save()

    return {'entity_link': entity_link, 'civ_id': civ_id}

def save_site_link(element, hf):
    civ_id, site_id, link_type, structure_id = None, None, None, None
    missing_fkeys = []
    for child in element:
        tag = child.tag.strip()
        if tag == 'entity_id':
            civ_id = child.text
        elif tag == 'site_id':
            site_id = child.text
        elif tag == 'link_type':
            link_type = child.text
        elif tag == 'sub_id':
            structure_id = child.text
        elif tag == 'occupation_id':
            pass
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Site Link: ' + tag + '\n')
    
    site_link = models.SiteLink.objects.create(world=hf.world, hf_id=hf, link_type=link_type)
    site_link.save()

    if site_id:
        missing_fkeys.append({'site_link': site_link, 'site_id': site_id})
    if civ_id:
        missing_fkeys.append({'site_link': site_link, 'civ_id': civ_id})
    if structure_id:
        missing_fkeys.append({'site_link': site_link, 'structure': [structure_id, site_id]})
    return missing_fkeys

def save_hf_skill(element, hf):
    skill, total_ip = None, None
    for child in element:
        tag = child.tag.strip()
        if tag == 'skill':
            skill = child.text
        elif tag == 'total_ip':
            total_ip = child.text
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save HF Skill: ' + tag + '\n')
    
    hf_skill = models.HfSkill.objects.create(world=hf.world, hf_id=hf, skill=skill, total_ip=total_ip)
    hf_skill.save()

def save_hf_link(element, hf):
    hf_id, link_type, link_strength = None, None, None
    for child in element:
        tag = child.tag.strip()
        if tag == 'hfid':
            hf_id = child.text
        elif tag == 'link_type':
            link_type = child.text
        elif tag == 'link_strength':
            link_strength = child.text
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save HF Link: ' + tag + '\n')

    hf_link = models.HfLink.objects.create(world=hf.world, hf_origin_id=hf, link_type=link_type, link_strength=link_strength)
    hf_link.save()

    return {'hf_link': hf_link, 'hf_id': hf_id}

def save_entity_former_position_link(element, hf):
    civ_id, end_year, position_id, start_year = None, None, None, None
    for child in element:
        tag = child.tag.strip()
        if tag == 'entity_id':
            civ_id = child.text
        elif tag == 'end_year':
            end_year = child.text
        elif tag == 'position_profile_id':
            position_id = child.text
        elif tag == 'start_year':
            start_year = child.text
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Entity Position Link: ' + tag + '\n')

    entity_position_link = models.EntityFormerPositionLink.objects.create(world=hf.world, hf_id=hf, start_year=start_year, end_year=end_year)
    entity_position_link.save()

    return {'entity_position_link': entity_position_link, 'position_id': position_id, 'civ_id': civ_id}
    
def save_relationship_profile_visual(element, hf):
    target_hfid, fear, last_meet_year, love, loyalty, meet_count, respect, trust, known_identity, rep_friendly, rep_information_source = None, None, None, None, None, None, None, None, None, None, None
    for child in element:
        tag = child.tag.strip()
        if tag == 'hf_id':
            target_hfid = child.text
        elif tag == 'fear':
            fear = child.text
        elif tag == 'last_meet_year':
            last_meet_year = child.text
        elif tag == 'love':
            love = child.text
        elif tag == 'loyalty':
            loyalty = child.text
        elif tag == 'meet_count':
            meet_count = child.text
        elif tag == 'respect':
            respect = child.text
        elif tag == 'trust':
            trust = child.text
        elif tag == 'rep_information_source':
            rep_information_source = child.text
        elif tag == 'last_meet_seconds72':
            pass
        elif tag == 'known_identity_id':
            known_identity = child.text
        elif tag == 'rep_friendly':
            rep_friendly = child.text
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Relationship Profile Visual: ' + tag + '\n')
    
    relationship_profile_visual = models.RelationshipProfileVisual.objects.create(world=hf.world, source_hfid=hf, fear=fear, last_meet_year=last_meet_year, love=love, loyalty=loyalty, meet_count=meet_count, respect=respect, trust=trust,  rep_friendly=rep_friendly, rep_information_source=rep_information_source)
    relationship_profile_visual.save()

    return {'relationship_profile_visual': relationship_profile_visual, 'target_hfid': target_hfid, 'known_identity': known_identity}

def save_intrigue_plot(element, hf):
    local_id, type, on_hold, civ_iv, artifact, actor_id, delegated_plot_hfid = None, None, None, None, None, None, None
    plot_actors = []
    missing_fkeys = []
    for child in element:
        tag = child.tag.strip()
        if tag == 'local_id':
            local_id = child.text
        elif tag == 'type':
            type = child.text
        elif tag == 'on_hold':
            on_hold = True
        elif tag == 'entity_id':
            civ_iv = child.text
        elif tag == 'artifact_id':
            artifact = child.text
        elif tag == 'actor_id':
            actor_id = child.text
        elif tag == 'delegated_plot_hfid':
            delegated_plot_hfid = child.text
        elif tag == 'plot_actor':
            plot_actors.append(child)
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Intrigue Plot: ' + tag + '\n')
    
    intrigue_plot = models.IntriguePlot.objects.create(world=hf.world, local_id=local_id, source_hfid=hf, type=type, on_hold=on_hold,)
    intrigue_plot.save()

    missing_fkeys.append({'intrigue_plot': intrigue_plot, 'civ_iv': civ_iv, 'artifact': artifact, 'actor_id': actor_id, 'delegated_plot_hfid': delegated_plot_hfid})

    if len(plot_actors) > 0:
        for actor in plot_actors:
            lists = save_plot_actor(actor, intrigue_plot)
            if lists:
                for dict in lists:
                    missing_fkeys.append(dict)
    return missing_fkeys

def save_plot_actor(element, plot):
    actor_id, plot_role, delegated_hfid, type, has_messenger = None, None, None, None, None
    for child in element:
        tag = child.tag.strip()
        if tag == 'actor_id':
            actor_id = child.text
        elif tag == 'plot_role':
            plot_role = child.text
        elif tag == 'delegated_plot_hfid':
            delegated_hfid = child.text
        elif tag == 'type':
            type = child.text
        elif tag == 'agreement_has_messenger':
            has_messenger = True
        elif tag == 'agreement_id':
            pass
        elif tag == 'handle_actor_id':
            pass
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Plot Actor: ' + tag + '\n')
    
    plot_actor = models.PlotActor.objects.create(world=plot.world, plot=plot, plot_role=plot_role, type=type, has_messenger=has_messenger)
    plot_actor.save()

    return {'plot_actor': plot_actor, 'actor_id': actor_id, 'delegated_hfid': delegated_hfid}


def save_intrigue_actor(element, hf):
    local_id, target_hfid, role, strategy, civ_id = None, None, None, None, None
    for child in element:
        tag = child.tag.strip()
        if tag == 'local_id':
            local_id = child.text
        elif tag == 'hfid':
            target_hfid = child.text
        elif tag == 'role':
            role = child.text
        elif tag == 'strategy':
            strategy = child.text
        elif tag == 'entity_id':
            civ_id = child.text
        elif tag == 'handle_actor_id':
            pass
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Intrigue Actor: ' + tag + '\n')
    
    intrigue_actor = models.IntrigueActor.objects.create(world=hf.world, local_id=local_id, source_hfid=hf, role=role, strategy=strategy)
    intrigue_actor.save()

    return {'intrigue_actor': intrigue_actor, 'target_hfid': target_hfid, 'civ_id': civ_id}

def save_entity_position_link(element, hf):
    position_id, start_year, civ_id = None, None, None
    for child in element:
        tag = child.tag.strip()
        if tag == 'position_profile_id':
            position_id = child.text
        elif tag == 'start_year':
            start_year = child.text
        elif tag == 'entity_id':
            civ_id = child.text
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Entity Position Link: ' + tag + '\n')
    
    entity_position_link = models.EntityPositionLink.objects.create(world=hf.world, hf_id=hf, start_year=start_year)
    entity_position_link.save()

    return {'entity_position_link': entity_position_link, 'position_id': position_id, 'civ_id': civ_id}

def save_vague_relationship(element, hf):
    exclude_tags = ['childhood_friend', 'athlete_buddy', 'war_buddy', 'jealous_obsession', 'artistic_buddy', 'scholar_buddy']
    target_hfid, type = None, None
    type = element[0].tag.strip()
    for child in element:
        tag = child.tag.strip()
        if tag == 'hfid':
            target_hfid = child.text
        elif tag in exclude_tags:
            pass
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Vague Relationship: ' + tag + '\n')
    
    vague_relationship = models.VagueRelationship.objects.create(world=hf.world, source_hfid=hf, type=type)
    vague_relationship.save()

    return {'vague_relationship': vague_relationship, 'target_hfid': target_hfid}

def save_entity_squad_link(element, hf):
    squad_id, squad_position, civ_id, start_year = None, None, None, None
    for child in element:
        tag = child.tag.strip()
        if tag == 'squad_id':
            squad_id = child.text
        elif tag == 'squad_position':
            squad_position = child.text
        elif tag == 'entity_id':
            civ_id = child.text
        elif tag == 'start_year':
            start_year = child.text
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Entity Squad Link: ' + tag + '\n')
    
    entity_squad_link = models.EntitySquadLink.objects.create(world=hf.world, hf_id=hf, squad_id=squad_id, squad_position=squad_position, start_year=start_year)
    entity_squad_link.save()

    return {'entity_squad_link': entity_squad_link, 'civ_id': civ_id}

def save_artifact(element, world):
    artifact_arguments = []

    chronicle_id, name, name2, missing_site_id, missing_holder_id, page_number, missing_written_content_id, item_type, material, item_subtype, item_description, missing_structure_local_id = None, None, None, None, None, None, None, None, None, None, None, None
    for child in element:
        if child.tag == 'id':
            chronicle_id = int(child.text)
        elif child.tag == 'name':
            name = child.text
        elif child.tag == 'item':
            for subchild in child:
                if subchild.tag == 'name_string':
                    name2 = subchild.text
                elif subchild.tag == 'page_number':
                    page_number = int(subchild.text)
                elif subchild.tag == 'page_written_content_id' or subchild.tag == 'writing_written_content_id':
                    # place in missing_fkeys, WrittenContent's are not saved yet
                    missing_written_content_id = int(subchild.text)
        elif child.tag == 'site_id':
            # Sites should be saved at this point, so we can use the fkey
            # Commenting out for now for testing
            # site = models.Sites.objects.get(chronicle_id=int(child.text))
            # artifact_arguments.append({'site': site})
            missing_site_id = int(child.text)
        elif child.tag == 'holder_hfid':
            # place in missing_fkeys, HistoricalFigure's are not saved yet
            missing_holder_id = int(child.text)
        elif child.tag == 'item_type':
            item_type = child.text
        elif child.tag == 'mat':
            material = child.text
        elif child.tag == 'item_subtype':
            item_subtype = child.text
        elif child.tag == 'item_description':
            item_description = child.text
        elif child.tag == 'structure_local_id':
            missing_structure_local_id = int(child.text)
        elif child.tag == 'page_count' or child.tag == 'writing' or child.tag == 'abs_tile_x' or child.tag == 'abs_tile_y' or child.tag == 'abs_tile_z':
            pass
        else:
            open('log.txt', 'a').write('!UNUSED TAG! Save Artifact: ' + child.tag + '\n')
        

    try:
        artifact = models.Artifact.objects.get(world=world, chronicle_id=chronicle_id)
        exists = True
    except models.Artifact.DoesNotExist:
        exists = False

    if exists:
        # Artifact has been seen before, update it
        if item_type:
            artifact.item_type = item_type
        if material:
            artifact.material = material
        if item_subtype:
            artifact.item_subtype = item_subtype
        if item_description:
            artifact.item_description = item_description
        artifact.save()
        # artifact = models.Artifact.objects.filter(world=world, chronicle_id=chronicle_id)
        pass
    else:
        # Artifact has not been seen before, create it
        artifact_arguments.append({'world' : world, 'chronicle_id': chronicle_id, 'name': name, 'name2': name2, 'page_number': page_number, 'item_type': item_type, 'material': material, 'item_subtype': item_subtype, 'item_description': item_description})

        artifact = models.Artifact.objects.create(**artifact_arguments[0])
        artifact.save()


        missing = {'artifact': artifact}
        if missing_site_id:
            missing['site'] = missing_site_id
        if missing_holder_id:
            missing['holder_id'] = missing_holder_id
        if missing_written_content_id:
            missing['written_content_id'] = missing_written_content_id
        if missing_structure_local_id:
            missing['structure_local_id'] = missing_structure_local_id

        return missing

def save_entity(element, world):
    chronicle_id, name, race, type, profession, weapon = None, None, None, None, None, None
    entity_positions = []
    entity_position_assignments = []
    occasions = []
    missing_fkeys = []
    worship_ids = []
    for child in element:
        if child.tag == 'id':
            chronicle_id = int(child.text)
        elif child.tag == 'name':
            name = child.text
        elif child.tag == 'race':
            race = child.text
        elif child.tag == 'type':
            type = child.text
        elif child.tag == 'entity_position':
            entity_positions.append(child)
        elif child.tag == 'entity_position_assignment':
            entity_position_assignments.append(child)
        elif child.tag == 'occasion':
            occasions.append(child)
        elif child.tag == 'profession':
            profession = child.text
        elif child.tag == 'weapon':
            weapon = child.text
        elif child.tag == 'worship_id':
            worship_ids.append(int(child.text))
        elif child.tag == 'child' or child.tag == 'entity_link' or child.tag == 'histfig_id' or child.tag == 'honor':
            pass
        else:
            open('log.txt', 'a').write('!UNUSED TAG! Save Entity: ' + child.tag + '\n')
    
    try:
        entity = models.Entities.objects.get(world=world, chronicle_id=chronicle_id)
        exists = True
    except models.Entities.DoesNotExist:
        exists = False
    
    if exists:
        if race:
            entity.race = race
        if type:
            entity.type = type
        if profession:
            entity.profession = profession
        if weapon:
            entity.weapon = weapon
        for position in entity_positions:
            save_entity_position(position, entity)
        for assignment in entity_position_assignments:
            lists = save_entity_position_assignment(assignment, entity)
            if lists:
                missing_fkeys.append(lists)
        for occasion in occasions:
            lists = save_occasion(occasion, entity)
            if lists:
                for dict in lists:
                    missing_fkeys.append(dict)
        entity.save()

        
    else:
        entity = models.Entities.objects.create(world=world, chronicle_id=chronicle_id, name=name)
        entity.save()
    
    for worship_id in worship_ids:
        missing_fkeys.append({'entity': entity, 'worship_id': worship_id})

    if missing_fkeys:
        return missing_fkeys
        
def save_entity_position(position, entity):
    world = entity.world
    civ_id = entity
    civ_position_id, name, name_male, name_female, spouse, spouse_male, spouse_female = None, None, None, None, None, None, None
    for child in position:
        tag = child.tag.strip()
        if tag == 'id':
            civ_position_id = child.text
        elif tag == 'name':
            name = child.text
        elif tag == 'name_male':
            name_male = child.text
        elif tag == 'name_female':
            name_female = child.text
        elif tag == 'spouse':
            spouse = child.text
        elif tag == 'spouse_male':
            spouse_male = child.text
        elif tag == 'spouse_female':
            spouse_female = child.text
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Entity Position: ' + tag + '\n')

    entity_position = models.EntityPosition.objects.create(world=world, civ_position_id=civ_position_id, civ_id=civ_id, name=name, name_male=name_male, name_female=name_female, spouse=spouse, spouse_male=spouse_male, spouse_female=spouse_female)
    entity_position.save()

def save_entity_position_assignment(assignment, entity):
    world = entity.world
    civ_id = entity
    hf_id, civ_position_assignment_id, position, squad_id = None, None, None, None
    for child in assignment:
        tag = child.tag.strip()
        if tag == 'id':
            civ_position_assignment_id = child.text
        elif tag == 'position_id':
            position = models.EntityPosition.objects.get(world=world, civ_id=civ_id, civ_position_id=child.text)
        elif tag == 'histfig':
            hf_id = child.text
        elif tag == 'squad_id':
            squad_id = child.text
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Entity Position Assignment: ' + tag + '\n')

    entity_position_assignment = models.EntityPositionAssignment.objects.create(world=world, civ_position_assignment_id=civ_position_assignment_id, civ_id=civ_id, position_id=position, squad_id=squad_id, hf_id=None)
    entity_position_assignment.save()
    
    if hf_id:
        missing = {'entity_position_assignment': entity_position_assignment, 'hf_id': hf_id}
        return missing

def save_occasion(occasion, entity):
    world = entity.world
    civ_id = entity
    schedules = []
    missing_fkeys = []
    civ_occasion_id, name= None, None
    for child in occasion:
        if child.tag == 'id':
            civ_occasion_id = child.text
        elif child.tag == 'name':
            name = child.text
        elif child.tag == 'schedule':
            schedules.append(child)
        elif child.tag == 'event':
            pass
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Occasion: ' + child.tag + '\n')

    occasion = models.Occasion.objects.create(world=world, civ_occasion_id=civ_occasion_id, civ_id=civ_id, name=name)
    occasion.save()
    for schedule in schedules:
        lists = save_schedule(schedule, occasion)
        if lists:
            for dict in lists:
                missing_fkeys.append(dict)

    if missing_fkeys:
        return missing_fkeys
        
def save_schedule(schedule, occasion):
    world = occasion.world
    references = []
    features = []
    missing_fkeys = []
    occasion_schedule_id, type, item_type, item_subtype = None, None, None, None
    for child in schedule:
        tag = child.tag.strip()
        if tag == 'id':
            occasion_schedule_id = child.text
        elif tag == 'type':
            type = child.text
        elif tag == 'reference':
            if int(child.text) == -1:
                pass
            else:
                references.append(child.text)
        elif tag == 'item_type':
            item_type = child.text
        elif tag == 'item_subtype':
            item_subtype = child.text
        elif tag == 'feature':
            features.append(child)
        elif tag == 'reference2':
            pass
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Schedule: ' + tag + '\n')

    schedule = models.Schedule.objects.create(world=world, occasion_schedule_id=occasion_schedule_id, occasion=occasion, type=type, item_type=item_type, item_subtype=item_subtype)
    schedule.save()

    for feature in features:
        lists = save_feature(feature, schedule)
        if lists:
            for dict in lists:
                missing_fkeys.append(dict)

    for reference in references:
        missing_fkeys.append({'schedule': schedule, 'reference': reference})

    if missing_fkeys:
        return missing_fkeys

def save_feature(feature, schedule):
    world = schedule.world
    references = []
    missing_fkeys = []
    type = None
    for child in feature:
        tag = child.tag.strip()
        if tag == 'type':
            type = child.text
        elif tag == 'reference':
            if int(child.text) == -1:
                pass
            else:
                references.append(child.text)
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Feature: ' + tag + '\n')
    
    feature = models.Feature.objects.create(world=world, schedule=schedule, type=type)
    feature.save()

    for reference in references:
        missing_fkeys.append({'feature': feature, 'reference': reference})

    if missing_fkeys:
        return missing_fkeys
    
def save_historical_era(element, world):
    name, start_year, end_year = None, None, None
    for child in element:
        tag = child.tag.strip()
        if tag == 'name':
            name = child.text
        elif tag == 'start_year':
            start_year = child.text
        elif tag == 'end_year':
            end_year = child.text
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Historical Era: ' + tag + '\n')
    
    historical_era = models.HistoricalEras.objects.create(world=world, name=name, start_year=start_year, end_year=end_year)
    historical_era.save()

def save_entity_population(element, world):
    civ_id, chronicle_id, race, population = None, None, None, None
    for child in element:
        tag = child.tag.strip()
        if tag == 'id':
            chronicle_id = child.text
        elif tag == 'civ_id':
            civ_id = child.text
        elif tag == 'race':
            split = child.text.split(':')
            race, population = split[0], split[1]
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Entity Population: ' + tag + '\n')
        
    try:
        entity_pop = models.EntityPopulations.objects.get(world=world, chronicle_id=chronicle_id)
        exists = True
    except models.EntityPopulations.DoesNotExist:
        exists = False

    if exists:
        civ_id = models.Entities.objects.get(world=world, chronicle_id=civ_id)
        entity_pop.civ_id = civ_id
        if race:
            entity_pop.race = race
        if population:
            entity_pop.population = population
        entity_pop.save()
    else:
        entity_pop = models.EntityPopulations.objects.create(world=world, chronicle_id=chronicle_id, race=race, population=population)
        entity_pop.save()

        if civ_id:
            return {'entity_pop': entity_pop, 'civ_id': civ_id}
        
def save_historical_event_collection(element, world):
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
        missing.append({'event_collection': event_collection, 'civ_id': civ_id})
    if site_id:
        missing.append({'event_collection': event_collection, 'site_id': site_id})
    if aggressor_entity_id:
        missing.append({'event_collection': event_collection, 'aggressor_entity_id': aggressor_entity_id})
    if defender_entity_id:
        missing.append({'event_collection': event_collection, 'defender_entity_id': defender_entity_id})
    if attacking_squad_site:
        missing.append({'event_collection': event_collection, 'attacking_squad_site': attacking_squad_site})
    if defending_squad_site:
        missing.append({'event_collection': event_collection, 'defending_squad_site': defending_squad_site})
    if len(attacking_hfids) > 0:
        for hf_id in attacking_hfids:
            missing.append({'event_collection': event_collection, 'attacking_hfid': hf_id})
    if len(defending_hfids) > 0:
        for hf_id in defending_hfids:
            missing.append({'event_collection': event_collection, 'defending_hfid': hf_id})
    if len(noncom_hfids) > 0:
        for hf_id in noncom_hfids:
            missing.append({'event_collection': event_collection, 'noncom_hfid': hf_id})
    if len(events) > 0:
        for event in events:
            missing.append({'event_collection': event_collection, 'event': event})
    if target_entity_id:
        missing.append({'event_collection': event_collection, 'target_entity_id': target_entity_id})
    
    if missing:
        return missing