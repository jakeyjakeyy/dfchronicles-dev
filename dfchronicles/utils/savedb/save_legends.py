from .historical_figure import save_historical_figure
from .artifact import save_artifact
from .entity import save_entity, save_entity_population
from .historical_era import save_historical_era
from .historical_event_collection import save_historical_event_collection
from .historical_event import save_historical_event
from .site import save_site
from .region import save_region
from .underground_region import save_underground_region
from .world_construction import save_world_construction
from .written_content import save_written_content
from .form import save_form
from .landmass import save_landmass
from .mountain_peak import save_mountain_peak
from .identity import save_identity


def SaveLegends(root, world):
    exclude_tags = ['start_seconds72', 'end_seconds72', 'birth_seconds72', 'death_seconds72', 'author_roll', 'form_id', 'coords', 'rectangle']
    class_tags = ['artifacts', 'entity_populations', 'historical_eras', 'historical_event_collections', 'historical_events', 'sites', 'regions', 'underground_regions', 'world_constructions', 'written_contents', 'poetic_forms', 'musical_forms', 'dance_forms', 'landmasses', 'mountain_peaks', 'identities']
    
    missing_fkeys = []

    # Find all elements and run associated save function
    def save_element(element, world):
        # Historical Figures and Entities are saved first to minimize uninitialized foreign keys
        hf = element.find('historical_figures')
        if hf:
            open('log.txt', 'a').write('Saving Historical Figures...\n')
            for child in hf:
                lists = save_historical_figure(child, world)
                if lists:
                    for dict in lists:
                        missing_fkeys.append(dict)
        ent = element.find('entities')
        if ent:
            open('log.txt', 'a').write('Saving Entities...\n')
            for child in ent:
                lists = save_entity(child, world)
                if lists:
                    for dict in lists:
                        missing_fkeys.append(dict)
        # Save remaining elements
        for child in element:
            if child.tag not in exclude_tags and child.tag in class_tags:
                open('log.txt', 'a').write('Saving ' + child.tag + '...\n')
                save_element(child, world)
            else:
                if child.tag == 'artifact':
                    lists = save_artifact(child, world)
                    if lists:
                        missing_fkeys.append(lists)
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
                elif child.tag == 'historical_event':
                    lists = save_historical_event(child, world)
                    if lists:
                        for dict in lists:
                            missing_fkeys.append(dict)
                elif child.tag == 'site':
                    lists = save_site(child, world)
                    if lists:
                        missing_fkeys.append(lists)
                elif child.tag == 'region':
                    lists = save_region(child, world)
                    if lists:
                        missing_fkeys.append(lists)
                elif child.tag == 'underground_region':
                    lists = save_underground_region(child, world)
                    if lists:
                        missing_fkeys.append(lists)
                elif child.tag == 'world_construction':
                    if len(child) > 0:
                        lists = save_world_construction(child, world)
                        if lists:
                            missing_fkeys.append(lists)
                elif child.tag == 'written_content':
                    lists = save_written_content(child, world)
                    if lists:
                        missing_fkeys.append(lists)
                elif child.tag == 'poetic_form':
                    save_form(child, world, 'poetic')
                elif child.tag == 'musical_form':
                    save_form(child, world, 'musical')
                elif child.tag == 'dance_form':
                    save_form(child, world, 'dance')
                elif child.tag == 'mountain_peak':
                    save_mountain_peak(child, world)
                elif child.tag == 'landmass':
                    save_landmass(child, world)
                elif child.tag == 'identity':
                    save_identity(child, world)

                else:
                    open('log.txt', 'a').write('!UNUSED CHILD! Save Legends: ' + child.tag + '\n')
    
    save_element(root, world)
    open('log.txt', 'a').write('Missing Foreign Keys: ' + str(missing_fkeys) + '\n')
