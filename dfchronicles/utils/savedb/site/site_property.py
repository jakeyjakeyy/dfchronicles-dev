def save_site_property(prop, site):
    from chronicle_compiler import models
    local_id, type, owner, structure_id = None, None, None, None

    for child in prop:
        tag = child.tag.strip()
        if tag == 'id':
            local_id = child.text
        elif tag == 'type':
            type = child.text
        elif tag == 'owner_hfid':
            owner = child.text
        elif tag == 'structure_id':
            structure_id = child.text
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Site Property: ' + child.tag + '\n')
    

    if owner:
        owner = models.HistoricalFigures.objects.get(world=site.world, chronicle_id=owner)
    if structure_id:
        structure_id = models.Structures.objects.get(world=site.world, structure_id=structure_id, site_id=site)
    property = models.SiteProperty.objects.create(world=site.world, site_id=site, local_id=local_id, type=type, owner=owner, structure_id=structure_id)
    property.save()