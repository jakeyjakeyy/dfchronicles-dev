def save_entity_population(element, world):
    from chronicle_compiler import models
    civ_id, chronicle_id, race, population = None, None, None, None
    for child in element:
        tag = child.tag.strip()
        if tag == 'id':
            chronicle_id = child.text
        elif tag == 'civ_id':
            civ_id = child.text
        elif tag == 'race':
            split = child.text.split(':')
            race, population = split[0], split[1]
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Entity Population: ' + tag + '\n')
        
    try:
        entity_pop = models.EntityPopulations.objects.get(world=world, chronicle_id=chronicle_id)
        exists = True
    except models.EntityPopulations.DoesNotExist:
        exists = False

    if exists:
        civ_id = models.Entities.objects.get(world=world, chronicle_id=civ_id)
        entity_pop.civ_id = civ_id
        if race:
            entity_pop.race = race
        if population:
            entity_pop.population = population
        entity_pop.save()
    else:
        entity_pop = models.EntityPopulations.objects.create(world=world, chronicle_id=chronicle_id, race=race, population=population)
        entity_pop.save()

        if civ_id:
            return {'entity_pop': entity_pop, 'civ_id': civ_id}
