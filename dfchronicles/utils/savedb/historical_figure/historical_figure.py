import cProfile
import pstats

from .entity_link import save_entity_link
from .site_link import save_site_link
from .hf_skill import save_hf_skill
from .hf_link import save_hf_link
from .entity_former_position_link import save_entity_former_position_link
from .relationship_profile_visual import save_relationship_profile_visual
from .plot import save_intrigue_plot
from .intrigue_actor import save_intrigue_actor
from .entity_position_link import save_entity_position_link
from .vague_relationship import save_vague_relationship
from .entity_squad_link import save_entity_squad_link

def save_historical_figure(element, world):
    from chronicle_compiler import models
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
    profiler = cProfile.Profile()
    profiler.enable()
    for child in element:
        tag = child.tag.strip()
        if tag in exclude_tags:
            continue
        match tag:
            case 'id':
                chronicle_id = child.text
            case 'appeared':
                appeared = child.text
            case 'associated_type':
                associated_type = child.text
            case 'birth_year':
                birth_year = child.text
            case 'caste':
                caste = child.text
            case 'death_year':
                if int(child.text) == -1:
                    death_year = None
                else:
                    death_year = child.text
            case 'deity':
                deity = True
            case 'goal':
                goal = child.text
            case 'name':
                name = child.text
            case 'race':
                race = child.text
            case 'used_identity_id':
                used_identities.append(child.text)
            case 'sphere':
                spheres.append(child.text)
            case 'journey_pet':
                journey_pet = child.text
            case 'ent_pop_id':
                ent_pop_id = child.text
            case 'current_identity_id':
                current_identity = child.text
            case 'holds_artifact':
                held_artifacts.append(child.text)
            case 'force':
                force = child.text
            case 'animated':
                animated = True
            case 'animated_string':
                animated_string = child.text
            case 'entity_link':
                entity_links.append(child)
            case 'site_link':
                site_links.append(child)
            case 'hf_skill':
                hf_skills.append(child)
            case 'hf_link':
                hf_links.append(child)
            case 'entity_former_position_link':
                former_positions.append(child)
            case 'relationship_profile_hf_visual':
                relationship_visuals.append(child)
            case 'intrigue_plot':
                intrigue_plots.append(child)
            case 'intrigue_actor':
                intrigue_actors.append(child)
            case 'entity_position_link':
                entity_positions_link.append(child)
            case 'vague_relationship':
                vague_relationships.append(child)
            case 'entity_squad_link':
                squad_links.append(child)
            case 'honor_entity':
                pass
            case 'site_property':
                pass
            case _:
                with open('log.txt', 'a') as log:
                    log.write('!UNUSED CHILD! Save Historical Figure: ' + tag + '\n')

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
                missing_fkeys.append(lists)
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
                missing_fkeys.append(links)
    if len(former_positions) > 0:
        for position in former_positions:
            links = save_entity_former_position_link(position, hf)
            if links:
                missing_fkeys.append(links)
    if len(relationship_visuals) > 0:
        for visual in relationship_visuals:
            links = save_relationship_profile_visual(visual, hf)
            if links:
                for link in links:
                    missing_fkeys.append(link)
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
                missing_fkeys.append(links)
    if len(vague_relationships) > 0:
        for relationship in vague_relationships:
            links = save_vague_relationship(relationship, hf)
            if links:
                missing_fkeys.append(links)
    if len(squad_links) > 0:
        for squad in squad_links:
            links = save_entity_squad_link(squad, hf)
            if links:
                missing_fkeys.append(links)


    if current_identity:
        missing_fkeys.append({'historicfigure': hf.id, 'current_identity': current_identity})
    if len(used_identities) > 0:
        for identity in used_identities:
            missing_fkeys.append({'historicfigure': hf.id, 'used_identity': identity})
    if len(held_artifacts) > 0:
        for artifact in held_artifacts:
            missing_fkeys.append({'historicfigure': hf.id, 'held_artifact': artifact})
    if ent_pop_id:
        missing_fkeys.append({'historicfigure': hf.id, 'ent_pop_id': ent_pop_id})
    

    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('cumulative')
    stats.dump_stats('historical_figure.prof')
    if missing_fkeys:
        return missing_fkeys