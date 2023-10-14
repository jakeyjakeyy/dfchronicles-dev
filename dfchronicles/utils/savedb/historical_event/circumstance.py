def save_circumstance(world, circumstance, he, circumstance_id):
    from chronicle_compiler import models
    if len(circumstance) > 0:
        for child in circumstance:
            if child.tag == 'type':
                type = child.text
            elif child.tag == 'hist_event_collection':
                hist_event_collection = child.text
        if type == 'histeventcollection':
            circumstance = models.Circumstance.objects.create(world=world, historical_event=he, hist_event_collection=hist_event_collection, type=type)
            he.circumstance = circumstance
            he.save()
        else:
            circumstance = models.Circumstance.objects.create(world=world, historical_event=he, type=type)
            he.circumstance = circumstance
            he.save()

    else:
        if circumstance.text == 'historical event collection':
            circumstance = models.Circumstance.objects.create(world=world, historical_event=he)
            he.circumstance = circumstance
            he.save()
            return {'circumstance': circumstance, 'hist_event_collection' : circumstance_id}
        else:
            circumstance = models.Circumstance.objects.create(world=world, historical_event=he, type=circumstance.text)