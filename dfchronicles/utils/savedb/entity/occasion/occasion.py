from .save_schedule import save_schedule

def save_occasion(occasion, entity):
    from chronicle_compiler import models
    world = entity.world
    civ_id = entity
    schedules = []
    missing_fkeys = []
    civ_occasion_id, name= None, None
    for child in occasion:
        if child.tag == 'id':
            civ_occasion_id = child.text
        elif child.tag == 'name':
            name = child.text
        elif child.tag == 'schedule':
            schedules.append(child)
        elif child.tag == 'event':
            pass
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Occasion: ' + child.tag + '\n')

    occasion = models.Occasion.objects.create(world=world, civ_occasion_id=civ_occasion_id, civ_id=civ_id, name=name)
    occasion.save()
    for schedule in schedules:
        lists = save_schedule(schedule, occasion)
        if lists:
            for dict in lists:
                missing_fkeys.append(dict)

    if missing_fkeys:
        return missing_fkeys
