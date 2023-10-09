def save_entity_squad_link(element, hf):
    from chronicle_compiler import models
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
