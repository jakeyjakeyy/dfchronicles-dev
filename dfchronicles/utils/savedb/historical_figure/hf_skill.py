def save_hf_skill(element, hf):
    from chronicle_compiler import models
    skill, total_ip = None, None
    for child in element:
        tag = child.tag.strip()
        if tag == 'skill':
            skill = child.text
        elif tag == 'total_ip':
            total_ip = child.text
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save HF Skill: ' + tag + '\n')
    
    hf_skill = models.HfSkill.objects.create(world=hf.world, hf_id=hf, skill=skill, total_ip=total_ip)
    hf_skill.save()
