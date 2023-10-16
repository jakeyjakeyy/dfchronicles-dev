def save_form(form, world, type):
    from chronicle_compiler import models
    chronicle_id, name, description = None, None, None

    for child in form:
        tag = child.tag.strip()
        if tag == 'id':
            chronicle_id = child.text
        elif tag == 'name':
            name = child.text
        elif tag == 'description':
            description = child.text
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! poetic_form: ' + tag + '\n')
        
    
    if type == 'poetic':
        try:
            poetic_form = models.PoeticForms.objects.get(
                world=world, chronicle_id=chronicle_id)
            poetic_form.name = name
            
        except models.PoeticForms.DoesNotExist:
            poetic_form = models.PoeticForms.objects.create(
                world=world, chronicle_id=chronicle_id, name=name,
                description=description)
            poetic_form.save()
    elif type == 'musical':
        try:
            musical_form = models.MusicalForms.objects.get(
                world=world, chronicle_id=chronicle_id)
            musical_form.name = name
            
        except models.MusicalForms.DoesNotExist:
            musical_form = models.MusicalForms.objects.create(
                world=world, chronicle_id=chronicle_id, name=name,
                description=description)
            musical_form.save()
    elif type == 'dance':
        try:
            dance_form = models.DanceForms.objects.get(
                world=world, chronicle_id=chronicle_id)
            dance_form.name = name
            
        except models.DanceForms.DoesNotExist:
            dance_form = models.DanceForms.objects.create(
                world=world, chronicle_id=chronicle_id, name=name,
                description=description)
            dance_form.save()