from .historical_figure import save_historical_figure
from .artifact import save_artifact
from .entity import save_entity, save_entity_population
from .historical_era import save_historical_era
from .historical_event_collection import save_historical_event_collection


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
