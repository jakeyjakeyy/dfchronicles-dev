from .plot_actor import save_plot_actor

def save_intrigue_plot(element, hf):
    from chronicle_compiler import models
    local_id, type, on_hold, civ_iv, artifact, actor_id, delegated_plot_hfid = None, None, None, None, None, None, None
    plot_actors = []
    missing_fkeys = []
    for child in element:
        tag = child.tag.strip()
        if tag == 'local_id':
            local_id = child.text
        elif tag == 'type':
            type = child.text
        elif tag == 'on_hold':
            on_hold = True
        elif tag == 'entity_id':
            civ_iv = child.text
        elif tag == 'artifact_id':
            artifact = child.text
        elif tag == 'actor_id':
            actor_id = child.text
        elif tag == 'delegated_plot_hfid':
            delegated_plot_hfid = child.text
        elif tag == 'plot_actor':
            plot_actors.append(child)
        elif tag == 'delegated_plot_id':
            pass
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Intrigue Plot: ' + tag + '\n')
    
    intrigue_plot = models.IntriguePlot.objects.create(world=hf.world, local_id=local_id, source_hfid=hf, type=type, on_hold=on_hold,)
    intrigue_plot.save()

    if civ_iv:
        missing_fkeys.append({'intrigue_plot': intrigue_plot, 'civ_iv': civ_iv})
    if artifact:
        missing_fkeys.append({'intrigue_plot': intrigue_plot, 'artifact': artifact})
    if actor_id:
        missing_fkeys.append({'intrigue_plot': intrigue_plot, 'actor_id': actor_id})
    if delegated_plot_hfid:
        missing_fkeys.append({'intrigue_plot': intrigue_plot, 'delegated_plot_hfid': delegated_plot_hfid})

    if len(plot_actors) > 0:
        for actor in plot_actors:
            lists = save_plot_actor(actor, intrigue_plot)
            if lists:
                missing_fkeys.append(lists)
    return missing_fkeys
