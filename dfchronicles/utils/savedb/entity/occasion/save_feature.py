def save_feature(feature, schedule):
    from chronicle_compiler import models
    world = schedule.world
    references = []
    missing_fkeys = []
    type = None
    for child in feature:
        tag = child.tag.strip()
        if tag == 'type':
            type = child.text
        elif tag == 'reference':
            if int(child.text) == -1:
                pass
            else:
                references.append(child.text)
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Feature: ' + tag + '\n')
    
    feature = models.Feature.objects.create(world=world, schedule=schedule, type=type)
    feature.save()

    # for reference in references:
    #     missing_fkeys.append({'feature': feature, 'reference': reference, 'type': type})

    if missing_fkeys:
        return missing_fkeys
 