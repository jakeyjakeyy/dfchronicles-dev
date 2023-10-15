from .structure import save_structure
from .site_property import save_site_property
def save_site(site, world):
    from chronicle_compiler import models
    chronicle_id, civ_id, cur_owner_id, name, type, coords, rectangle = None, None, None, None, None, None, None
    structures = []
    properties = []
    missing_fkeys = []

    for child in site:
        tag = child.tag.strip()
        if tag == 'id':
            chronicle_id = child.text
        elif tag == 'civ_id':
            civ_id = child.text
        elif tag == 'cur_owner_id':
            cur_owner_id = child.text
        elif tag == 'name':
            name = child.text
        elif tag == 'type':
            type = child.text
        elif tag == 'coords':
            coords = child.text
        elif tag == 'rectangle':
            rectangle = child.text
        elif tag == 'structures':
            for structure in child:
                structures.append(structure)
        elif tag == 'site_properties':
            for prop in child:
                properties.append(prop)
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Site: ' + child.tag + '\n')

    try:
        site = models.Sites.objects.get(world=world, chronicle_id=chronicle_id)
        if name:
            site.name = name
        if type:
            site.type = type
        if coords:
            site.coords = coords
        if rectangle:
            site.rectangle = rectangle
        site.save()

        if cur_owner_id:
            try:
                cur_owner_id = models.Entities.objects.get(world=world, chronicle_id=cur_owner_id)
                site.cur_owner_id = cur_owner_id
            except models.Entities.DoesNotExist:
                missing_fkeys.append({'site': site, 'cur_owner_id': cur_owner_id})
        if civ_id:
            try:
                civ_id = models.Entities.objects.get(world=world, chronicle_id=civ_id)
                site.civ_id = civ_id
            except models.Entities.DoesNotExist:
                missing_fkeys.append({'site': site, 'civ_id': civ_id})
        site.save()
    except models.Sites.DoesNotExist:
        site = models.Sites.objects.create(world=world, chronicle_id=chronicle_id, civ_id=civ_id, cur_owner_id=cur_owner_id, name=name, type=type, coords=coords, rectangle=rectangle)
        site.save()

    for structure in structures:
        save_structure(structure, site)
    for prop in properties:
        save_site_property(prop, site)

    if len(missing_fkeys) > 0:
        return missing_fkeys