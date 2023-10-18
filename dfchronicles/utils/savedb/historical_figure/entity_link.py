def save_entity_link(element, hf):
    from chronicle_compiler import models
    civ_id, link_type, link_strength = None, None, None
    for child in element:
        tag = child.tag.strip()
        if tag == 'entity_id':
            civ_id = child.text
        elif tag == 'link_type':
            link_type = child.text
        elif tag == 'link_strength':
            link_strength = child.text
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Entity Link: ' + tag + '\n')
    
    entity_link = models.EntityLink.objects.create(world=hf.world, hf_id=hf, link_type=link_type, link_strength=link_strength)
    entity_link.save()

    return {'entity_link': entity_link.id, 'civ_id': civ_id}
