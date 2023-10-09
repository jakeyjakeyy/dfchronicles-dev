def save_historical_era(element, world):
    from chronicle_compiler import models
    name, start_year, end_year = None, None, None
    for child in element:
        tag = child.tag.strip()
        if tag == 'name':
            name = child.text
        elif tag == 'start_year':
            start_year = child.text
        elif tag == 'end_year':
            end_year = child.text
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Historical Era: ' + tag + '\n')
    
    historical_era = models.HistoricalEras.objects.create(world=world, name=name, start_year=start_year, end_year=end_year)
    historical_era.save()
