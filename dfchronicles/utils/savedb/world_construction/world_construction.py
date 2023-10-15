def save_world_construction(construction, world):
    from chronicle_compiler import models
    chronicle_id, type, coords, name = None, None, None, None

    for child in construction:
        tag = child.tag.strip()
        if tag == 'id':
            chronicle_id = child.text
        elif tag == 'type':
            type = child.text
        elif tag == 'coords':
            coords = child.text
        elif tag == 'name':
            name = child.text
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save World Construction: ' + child.tag + '\n')
        
    try:
        con = models.WorldConstruction.objects.get(world=world, chronicle_id=chronicle_id)
        if type:
            con.type = type
        if coords:
            con.coords = coords
        if name:
            con.name = name
    except models.WorldConstruction.DoesNotExist:
        con = models.WorldConstruction.objects.create(world=world, chronicle_id=chronicle_id, type=type, coords=coords, name=name)