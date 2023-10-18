def save_entity_former_position_link(element, hf):
    from chronicle_compiler import models
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

    return {'entity_former_position_link': entity_position_link.id, 'position_id': position_id, 'civ_id': civ_id}
   