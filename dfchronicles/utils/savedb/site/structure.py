def save_structure(structure, site):
    from chronicle_compiler import models
    structure_id, type, name, name2 = None, None, None, None
    inhabitants = []
    for child in structure:
        tag = child.tag.strip()
        if tag == 'local_id':
            structure_id = child.text
        elif tag == 'type':
            type = child.text
        elif tag == 'name':
            name = child.text
        elif tag == 'name2':
            name2 = child.text
        elif tag == 'inhabitant':
            inhabitants.append(child.text)
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Structure: ' + child.tag + '\n')

    struct = models.Structures.objects.create(world=site.world, site_id=site, structure_id=structure_id, type=type, name=name, name2=name2)
    struct.save()

    for inhabitant in inhabitants:
        struct.inhabitants.add(models.HistoricalFigures.objects.get(world=site.world, chronicle_id=inhabitant))
    struct.save()