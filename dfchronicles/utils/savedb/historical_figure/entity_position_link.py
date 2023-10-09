def save_entity_position_link(element, hf):
    from chronicle_compiler import models
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
