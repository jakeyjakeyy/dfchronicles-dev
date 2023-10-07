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

    test_tags = ['artifacts', 'entities', 'entity_populations', 'historical_eras']

    # Find all elements and run associated save function
    def save_element(element, world):
        for child in element:
            if child.tag not in exclude_tags and child.tag in test_tags:
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
                else:
                    open('log.txt', 'a').write('!UNUSED CHILD! Save Legends: ' + child.tag + '\n')
    
    save_element(root, world)
    open('log.txt', 'a').write('Missing Foreign Keys: ' + str(missing_fkeys) + '\n')


    
# Save functions
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
        elif child.tag == 'page_count' or child.tag == 'writing':
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

entity_position_assignments = []
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
        elif child.tag == 'child' or child.tag == 'entity_link' or child.tag == 'histfig_id':
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