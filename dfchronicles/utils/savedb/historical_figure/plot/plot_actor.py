def save_plot_actor(element, plot):
    from chronicle_compiler import models
    actor_id, plot_role, delegated_hfid, type, has_messenger = None, None, None, None, None
    for child in element:
        tag = child.tag.strip()
        if tag == 'actor_id':
            actor_id = child.text
        elif tag == 'plot_role':
            plot_role = child.text
        elif tag == 'delegated_plot_hfid':
            delegated_hfid = child.text
        elif tag == 'type':
            type = child.text
        elif tag == 'agreement_has_messenger':
            has_messenger = True
        elif tag == 'agreement_id':
            pass
        elif tag == 'handle_actor_id':
            pass
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! Save Plot Actor: ' + tag + '\n')
    
    plot_actor = models.PlotActor.objects.create(world=plot.world, plot=plot, plot_role=plot_role, type=type, has_messenger=has_messenger)
    plot_actor.save()


    missing_fkeys = []

    if actor_id:
        missing_fkeys.append({'plot_actor': plot_actor.id, 'actor_id': actor_id})
    if delegated_hfid:
        missing_fkeys.append({'plot_actor': plot_actor.id, 'delegated_hfid': delegated_hfid})

    return missing_fkeys
