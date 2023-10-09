def save_entity_position(position, entity):
    from chronicle_compiler import models
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
