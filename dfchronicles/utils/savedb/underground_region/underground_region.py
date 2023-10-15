def save_underground_region(region, world):
    from chronicle_compiler import models
    chronicle_id, type, depth, coords = None, None, None, None

    for child in region:
        tag = child.tag.strip()
        if tag == 'id':
            chronicle_id = child.text
        elif tag == 'type':
            type = child.text
        elif tag == 'depth':
            depth = child.text
        elif tag == 'coords':
            coords = child.text
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Underground Region: ' + child.tag + '\n')

    try:
        reg = models.UndergroundRegions.objects.get(world=world, chronicle_id=chronicle_id)
        if type:
            reg.type = type
        if depth:
            reg.depth = depth
        if coords:
            reg.coords = coords
    except models.UndergroundRegions.DoesNotExist:
        reg = models.UndergroundRegions.objects.create(world=world, chronicle_id=chronicle_id, type=type, depth=depth, coords=coords)
    
    reg.save()