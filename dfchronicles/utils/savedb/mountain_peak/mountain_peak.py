def save_mountain_peak(mountain, world):
    from chronicle_compiler import models
    chronicle_id, name, coords, height, volcano = None, None, None, None, None

    for child in mountain:
        tag = child.tag.strip()
        if tag == 'id':
            chronicle_id = child.text
        elif tag == 'name':
            name = child.text
        elif tag == 'coords':
            coords = child.text
        elif tag == 'height':
            height = child.text
        elif tag == 'is_volcano':
            volcano = True
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! mountain_peak: ' + tag + '\n')

    mp = models.MountainPeak.objects.create(world=world, chronicle_id=chronicle_id, name=name, coords=coords, height=height, volcano=volcano)
    mp.save()