def save_entity_position_assignment(assignment, entity):
    from chronicle_compiler import models
    world = entity.world
    civ_id = entity
    hf_id, civ_position_assignment_id, position, squad_id = None, None, None, None
    for child in assignment:
        tag = child.tag.strip()
        if tag == 'id':
            civ_position_assignment_id = child.text
        elif tag == 'position_id':
            position = models.EntityPosition.objects.get(world=world, civ_id=civ_id, civ_position_id=child.text)
        elif tag == 'histfig':
            hf_id = child.text
        elif tag == 'squad_id':
            squad_id = child.text
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Entity Position Assignment: ' + tag + '\n')

    entity_position_assignment = models.EntityPositionAssignment.objects.create(world=world, civ_position_assignment_id=civ_position_assignment_id, civ_id=civ_id, position_id=position, squad_id=squad_id, hf_id=None)
    entity_position_assignment.save()
    
    if hf_id:
        try:
            hf = models.HistoricalFigures.objects.get(world=world, chronicle_id=hf_id)
            entity_position_assignment.hf_id = hf
            entity_position_assignment.save()
        except models.HistoricalFigures.DoesNotExist:
            missing = {'entity_position_assignment': entity_position_assignment, 'hf_id': hf_id}
            return missing
