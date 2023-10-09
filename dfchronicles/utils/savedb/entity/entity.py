from .entity_position import save_entity_position, save_entity_position_assignment
from .occasion import save_occasion

def save_entity(element, world):
    from chronicle_compiler import models
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
   