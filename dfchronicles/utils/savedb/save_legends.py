import time

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

    # timer elements
    hf_timer = {'count': 0, 'time': 0}
    ent_timer = {'count': 0, 'time': 0}
    art_timer = {'count': 0, 'time': 0}
    entpop_timer = {'count': 0, 'time': 0}
    he_timer = {'count': 0, 'time': 0}
    hec_timer = {'count': 0, 'time': 0}
    writtencontent_timer = {'count': 0, 'time': 0}

    # Find all elements and run associated save function
    def save_element(element, world):
        # Historical Figures and Entities are saved first to minimize uninitialized foreign keys
        hf = element.find('historical_figures')
        if hf:
            open('log.txt', 'a').write('Saving Historical Figures...\n')
            for child in hf:
                start_time = time.perf_counter()
                lists = save_historical_figure(child, world)
                if lists:
                    for dict in lists:
                        missing_fkeys.append(dict)
                end_time = time.perf_counter()
                hf_timer['count'] += 1
                hf_timer['time'] += end_time - start_time
        ent = element.find('entities')
        if ent:
            open('log.txt', 'a').write('Saving Entities...\n')
            for child in ent:
                start_time = time.perf_counter()
                lists = save_entity(child, world)
                if lists:
                    for dict in lists:
                        missing_fkeys.append(dict)
                end_time = time.perf_counter()
                ent_timer['count'] += 1
                ent_timer['time'] += end_time - start_time
        # Save remaining elements
        for child in element:
            if child.tag not in exclude_tags and child.tag in class_tags:
                open('log.txt', 'a').write('Saving ' + child.tag + '...\n')
                save_element(child, world)
            else:
                if child.tag == 'artifact':
                    start_time = time.perf_counter()
                    lists = save_artifact(child, world)
                    if lists:
                        for dict in lists:
                            missing_fkeys.append(dict)
                    end_time = time.perf_counter()
                    art_timer['count'] += 1
                    art_timer['time'] += end_time - start_time
                elif child.tag == 'entity_population':
                    start_time = time.perf_counter()
                    lists = save_entity_population(child, world)
                    if lists:
                        missing_fkeys.append(lists)
                    end_time = time.perf_counter()
                    entpop_timer['count'] += 1
                    entpop_timer['time'] += end_time - start_time
                elif child.tag == 'historical_era':
                    save_historical_era(child, world)
                elif child.tag == 'historical_event_collection':
                    start_time = time.perf_counter()
                    lists = save_historical_event_collection(child, world)
                    if lists:
                        for dict in lists:
                            missing_fkeys.append(dict)
                    end_time = time.perf_counter()
                    hec_timer['count'] += 1
                    hec_timer['time'] += end_time - start_time
                elif child.tag == 'historical_event':
                    start_time = time.perf_counter()
                    lists = save_historical_event(child, world)
                    if lists:
                        for dict in lists:
                            missing_fkeys.append(dict)
                    end_time = time.perf_counter()
                    he_timer['count'] += 1
                    he_timer['time'] += end_time - start_time
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
                    start_time = time.perf_counter()
                    lists = save_written_content(child, world)
                    if lists:
                        for dict in lists:
                            missing_fkeys.append(dict)
                    end_time = time.perf_counter()
                    writtencontent_timer['count'] += 1
                    writtencontent_timer['time'] += end_time - start_time
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

    with open('timer.txt', 'a') as timer:
        if hf_timer != {'count': 0, 'time': 0}:
            hf_avg = hf_timer['time'] / hf_timer['count']
            timer.write('Historical Figure Average: ' + str(hf_avg) + '\n')
        if ent_timer != {'count': 0, 'time': 0}:
            ent_avg = ent_timer['time'] / ent_timer['count']
            timer.write('Entity Average: ' + str(ent_avg) + '\n')
        if art_timer != {'count': 0, 'time': 0}:
            art_avg = art_timer['time'] / art_timer['count']
            timer.write('Artifact Average: ' + str(art_avg) + '\n')
        if entpop_timer != {'count': 0, 'time': 0}:
            entpop_avg = entpop_timer['time'] / entpop_timer['count']
            timer.write('Entity Population Average: ' + str(entpop_avg) + '\n')
        if hec_timer != {'count': 0, 'time': 0}:
            hec_avg = hec_timer['time'] / hec_timer['count']
            timer.write('Historical Event Collection Average: ' + str(hec_avg) + '\n')
        if he_timer != {'count': 0, 'time': 0}:
            he_avg = he_timer['time'] / he_timer['count']
            timer.write('Historical Event Average: ' + str(he_avg) + '\n')
        if writtencontent_timer != {'count': 0, 'time': 0}:
            writtencontent_avg = writtencontent_timer['time'] / writtencontent_timer['count']
            timer.write('Written Content Average: ' + str(writtencontent_avg) + '\n\n')


    open('log.txt', 'a').write('Missing Foreign Keys: ' + str(missing_fkeys) + '\n')

    timer.close()
    return missing_fkeys