def save_region(region, world):
    from chronicle_compiler import models
    chronicle_id, name, type, evilness, force, coords = None, None, None, None, None, None
    for child in region:
        tag = child.tag.strip()
        if tag == 'id':
            chronicle_id = child.text
        elif tag == 'name':
            name = child.text
        elif tag == 'type':
            type = child.text
        elif tag == 'evilness':
            evilness = child.text
        elif tag == 'force_id':
            force = child.text
        elif tag == 'coords':
            coords = child.text
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Region: ' + child.tag + '\n')

    if force:
        force = models.HistoricalFigures.objects.get(world=world, chronicle_id=force)

    try:
        reg = models.Regions.objects.get(world=world, chronicle_id=chronicle_id)
        if name:
            reg.name = name
        if type:
            reg.type = type
        if evilness:
            reg.evilness = evilness
        if force:
            reg.force = force
        if coords:
            reg.coords = coords
    except models.Regions.DoesNotExist:
        reg = models.Regions.objects.create(world=world, chronicle_id=chronicle_id, name=name, type=type, evilness=evilness, force=force, coords=coords)

    reg.save()