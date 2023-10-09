def save_relationship_profile_visual(element, hf):
    from chronicle_compiler import models
    target_hfid, fear, last_meet_year, love, loyalty, meet_count, respect, trust, known_identity, rep_friendly, rep_information_source = None, None, None, None, None, None, None, None, None, None, None
    for child in element:
        tag = child.tag.strip()
        if tag == 'hf_id':
            target_hfid = child.text
        elif tag == 'fear':
            fear = child.text
        elif tag == 'last_meet_year':
            last_meet_year = child.text
        elif tag == 'love':
            love = child.text
        elif tag == 'loyalty':
            loyalty = child.text
        elif tag == 'meet_count':
            meet_count = child.text
        elif tag == 'respect':
            respect = child.text
        elif tag == 'trust':
            trust = child.text
        elif tag == 'rep_information_source':
            rep_information_source = child.text
        elif tag == 'last_meet_seconds72':
            pass
        elif tag == 'known_identity_id':
            known_identity = child.text
        elif tag == 'rep_friendly':
            rep_friendly = child.text
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Relationship Profile Visual: ' + tag + '\n')
    
    relationship_profile_visual = models.RelationshipProfileVisual.objects.create(world=hf.world, source_hfid=hf, fear=fear, last_meet_year=last_meet_year, love=love, loyalty=loyalty, meet_count=meet_count, respect=respect, trust=trust,  rep_friendly=rep_friendly, rep_information_source=rep_information_source)
    relationship_profile_visual.save()

    return {'relationship_profile_visual': relationship_profile_visual, 'target_hfid': target_hfid, 'known_identity': known_identity}
