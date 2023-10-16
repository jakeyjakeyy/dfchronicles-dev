def save_landmass(landmass, world):
    from chronicle_compiler import models
    chronicle_id, name, coord1, coord2 = None, None, None, None

    for child in landmass:
        tag = child.tag.strip()
        if tag == 'id':
            chronicle_id = child.text
        elif tag == 'name':
            name = child.text
        elif tag == 'coord_1':
            coord1 = child.text
        elif tag == 'coord_2':
            coord2 = child.text
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! landmass: ' + tag + '\n')

    landmass = models.Landmass.objects.create(world=world, chronicle_id=chronicle_id, name=name, coord1=coord1, coord2=coord2)
    landmass.save()