def save_structure(structure, site):
    from chronicle_compiler import models
    structure_id, type, name, name2, civ_id, subtype = None, None, None, None, None, None
    inhabitants = []
    for child in structure:
        tag = child.tag.strip()
        if tag == 'local_id' or tag == 'id':
            structure_id = child.text
        elif tag == 'type':
            type = child.text
        elif tag == 'name':
            name = child.text
        elif tag == 'name2':
            name2 = child.text
        elif tag == 'inhabitant':
            inhabitants.append(child.text)
        elif tag == 'entity_id' or tag == 'religion':
            civ_id = models.Entities.objects.get(world=site.world, chronicle_id=child.text)
        elif tag == 'subtype':
            subtype = child.text
        elif tag == 'deity_type' or tag == 'dungeon_type':
            pass
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Structure: ' + child.tag + '\n')


    try:
        struct = models.Structures.objects.get(world=site.world, site_id=site, structure_id=structure_id)
        if name2:
            struct.name2 = name2
        if inhabitants:
            for inhabitant in inhabitants:
                struct.inhabitant.add(models.HistoricalFigures.objects.get(world=site.world, chronicle_id=inhabitant))
        if structure_id:
            struct.structure_id = structure_id
    except models.Structures.DoesNotExist:
        struct = models.Structures.objects.create(world=site.world, site_id=site, structure_id=structure_id, type=type, name=name, name2=name2, civ_id=civ_id, subtype=subtype)

    struct.save()
