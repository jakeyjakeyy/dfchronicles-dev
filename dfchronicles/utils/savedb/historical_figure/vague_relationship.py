def save_vague_relationship(element, hf):
    from chronicle_compiler import models
    exclude_tags = ['childhood_friend', 'athlete_buddy', 'war_buddy', 'jealous_obsession', 'artistic_buddy', 'scholar_buddy', 'persecution_grudge', 'religious_persecution_grudge']
    target_hfid, type = None, None
    type = element[0].tag.strip()
    for child in element:
        tag = child.tag.strip()
        if tag == 'hfid':
            target_hfid = child.text
        elif tag in exclude_tags:
            pass
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Vague Relationship: ' + tag + '\n')
    
    vague_relationship = models.VagueRelationship.objects.create(world=hf.world, source_hfid=hf, type=type)
    vague_relationship.save()

    return {'vague_relationship': vague_relationship.id, 'target_hfid': target_hfid}
