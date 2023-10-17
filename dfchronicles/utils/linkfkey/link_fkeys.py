def link_fkeys(fkeys):
    for dict in fkeys:
        for key, value in dict.items():
            match key:
                case 'artifact':
                    match value:
                        case 'written_content_id':
                            ...
                        case _:
                            open('log.txt', 'a').write(f'!MISSING VALUE! link_fkeys - artifact: {value}\n')
                case 'historical_event':
                    match value:
                        case 'identity':
                            ...
                        case 'target_identity':
                            ...
                        case 'written_content':
                            ...
                        case 'musical_form':
                            ...
                        case 'poetic_form':
                            ...
                        case 'dance_form':
                            ...
                        case _:
                            open('log.txt', 'a').write(f'!MISSING VALUE! link_fkeys - historical_event: {value}\n')
                case 'historicfigure':
                    match value:
                        case 'current_identity':
                            ...
                        case 'used_identity':
                            ...
                        case 'held_artifact':
                            ...
                        case 'ent_pop_id':
                            ...
                        case _:
                            open('log.txt', 'a').write(f'!MISSING VALUE! link_fkeys - historicfigure: {value}\n')
                case 'entity_link':
                    # One child, pass value to save function
                    ...
                case 'site_link':
                    match value:
                        case 'site_id':
                            ...
                        case 'civ_id':
                            ...
                        case 'structure':
                            ...
                        case _:
                            open('log.txt', 'a').write(f'!MISSING VALUE! link_fkeys - site_link: {value}\n')
                case 'hf_link':
                    # One child, pass value to save function
                    ...
                case 'entity_former_position_link':
                    # One child, pass to save function
                    ...
                case 'relationship_profile_visual':
                    match value:
                        case 'target_hfid':
                            ...
                        case 'known_identity':
                            ...
                        case _:
                            open('log.txt', 'a').write(f'!MISSING VALUE! link_fkeys - relationship_profile_visual: {value}\n')
                case 'intrigue_plot':
                    match value:
                        case 'civ_id':
                            ...
                        case 'artifact':
                            ...
                        case 'actor_id':
                            ...
                        case 'delegated_plot_hfid':
                            ...
                        case _:
                            open('log.txt', 'a').write(f'!MISSING VALUE! link_fkeys - intrigue_plot: {value}\n')
                case 'intrigue_actor':
                    match value:
                        case 'target_hfid':
                            ...
                        case 'civ_id':
                            ...
                        case _:
                            open('log.txt', 'a').write(f'!MISSING VALUE! link_fkeys - intrigue_actor: {value}\n')
                case 'entity_position_link':
                    match value:
                        case 'position_id':
                            ...
                        case 'civ_id':
                            ...
                        case _:
                            open('log.txt', 'a').write(f'!MISSING VALUE! link_fkeys - entity_position_link: {value}\n')
                case 'vague_relationship':
                    # One child, pass to save function
                    ...
                case 'entity_squad_link':
                    # One child, pass to save function
                    ...
                case 'chronicle':
                    match value:
                        case 'musical':
                            ...
                        case 'poetic':
                            ...
                        case 'dance':
                            ...
                case _:
                    open('log.txt', 'a').write(f'!MISSING VALUE! link_fkeys: {key}\n')