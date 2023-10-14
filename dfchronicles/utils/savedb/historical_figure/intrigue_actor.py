def save_intrigue_actor(element, hf):
    from chronicle_compiler import models
    local_id, target_hfid, role, strategy, civ_id, promised_me_immortality, promised_actor_immortality = None, None, None, None, None, None, None
    for child in element:
        tag = child.tag.strip()
        if tag == 'local_id':
            local_id = child.text
        elif tag == 'hfid':
            target_hfid = child.text
        elif tag == 'role':
            role = child.text
        elif tag == 'strategy':
            strategy = child.text
        elif tag == 'entity_id':
            civ_id = child.text
        elif tag == 'handle_actor_id':
            pass
        elif tag == 'promised_actor_immortality':
            promised_actor_immortality = True
        elif tag == 'promised_me_immortality':
            promised_me_immortality = True
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Intrigue Actor: ' + tag + '\n')
    
    intrigue_actor = models.IntrigueActor.objects.create(world=hf.world, local_id=local_id, source_hfid=hf, role=role, strategy=strategy, promised_me_immortality=promised_me_immortality, promised_actor_immortality=promised_actor_immortality)
    intrigue_actor.save()

    missing_fkeys = []

    if target_hfid:
        missing_fkeys.append({'intrigue_actor': intrigue_actor, 'target_hfid': target_hfid})
    if civ_id:
        missing_fkeys.append({'intrigue_actor': intrigue_actor, 'civ_id': civ_id})

    return missing_fkeys
