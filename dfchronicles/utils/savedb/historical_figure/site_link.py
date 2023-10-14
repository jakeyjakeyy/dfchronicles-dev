def save_site_link(element, hf):
    from chronicle_compiler import models
    civ_id, site_id, link_type, structure_id = None, None, None, None
    missing_fkeys = []
    for child in element:
        tag = child.tag.strip()
        if tag == 'entity_id':
            civ_id = child.text
        elif tag == 'site_id':
            site_id = child.text
        elif tag == 'link_type':
            link_type = child.text
        elif tag == 'sub_id':
            structure_id = child.text
        elif tag == 'occupation_id':
            pass
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Site Link: ' + tag + '\n')
    
    site_link = models.SiteLink.objects.create(world=hf.world, hf_id=hf, link_type=link_type)
    site_link.save()

    if site_id:
        missing_fkeys.append({'site_link': site_link, 'site_id': site_id})
    if civ_id:
        missing_fkeys.append({'site_link': site_link, 'civ_id': civ_id})
    if structure_id:
        missing_fkeys.append({'site_link': site_link, 'structure': structure_id, 'site': site_id})
    return missing_fkeys
