def save_identity(identity, world):
    from chronicle_compiler import models

    chronicle_id, name, hf_id, birth_year, civ_id, nemesis, race, caste, profession = None, None, None, None, None, None, None, None, None

    for child in identity:
        tag = child.tag.strip()
        if tag == 'id':
            chronicle_id = child.text
        elif tag == 'name':
            name = child.text
        elif tag == 'histfig_id':
            hf_id = child.text
        elif tag == 'birth_year':
            if int(child.tag) >= 0:
                birth_year = child.text
        elif tag == 'entity_id':
            civ_id = models.Entities.objects.get(world=world, chronicle_id=child.text)
        elif tag == 'nemesis':
            nemesis = models.HistoricalFigures.objects.get(world=world, chronicle_id=child.text)
        elif tag == 'race':
            race = child.text
        elif tag == 'caste':
            caste = child.text
        elif tag == 'profession':
            profession = child.text
        elif tag == 'birth_second':
            pass
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! identity: ' + tag + '\n')
    
    identity = models.Identities.objects.create(world=world, chronicle_id=chronicle_id, name=name, hf_id=hf_id, birth_year=birth_year, civ_id=civ_id, nemesis=nemesis, race=race, caste=caste, profession=profession)