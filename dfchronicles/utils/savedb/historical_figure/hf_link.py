def save_hf_link(element, hf):
    from chronicle_compiler import models
    hf_id, link_type, link_strength = None, None, None
    for child in element:
        tag = child.tag.strip()
        if tag == 'hfid':
            hf_id = child.text
        elif tag == 'link_type':
            link_type = child.text
        elif tag == 'link_strength':
            link_strength = child.text
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save HF Link: ' + tag + '\n')

    hf_link = models.HfLink.objects.create(world=hf.world, hf_origin_id=hf, link_type=link_type, link_strength=link_strength)
    hf_link.save()

    return {'hf_link': hf_link, 'hf_id': hf_id}
