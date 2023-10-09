from .save_feature import save_feature


def save_schedule(schedule, occasion):
    from chronicle_compiler import models
    world = occasion.world
    references = []
    features = []
    missing_fkeys = []
    occasion_schedule_id, type, item_type, item_subtype = None, None, None, None
    for child in schedule:
        tag = child.tag.strip()
        if tag == 'id':
            occasion_schedule_id = child.text
        elif tag == 'type':
            type = child.text
        elif tag == 'reference':
            if int(child.text) == -1:
                pass
            else:
                references.append(child.text)
        elif tag == 'item_type':
            item_type = child.text
        elif tag == 'item_subtype':
            item_subtype = child.text
        elif tag == 'feature':
            features.append(child)
        elif tag == 'reference2':
            pass
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Schedule: ' + tag + '\n')

    schedule = models.Schedule.objects.create(world=world, occasion_schedule_id=occasion_schedule_id, occasion=occasion, type=type, item_type=item_type, item_subtype=item_subtype)
    schedule.save()

    for feature in features:
        lists = save_feature(feature, schedule)
        if lists:
            for dict in lists:
                missing_fkeys.append(dict)

    for reference in references:
        missing_fkeys.append({'schedule': schedule, 'reference': reference})

    if missing_fkeys:
        return missing_fkeys
