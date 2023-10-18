debug = True
def link_fkeys(fkeys, world):
    from chronicle_compiler import models
    for dict in fkeys:
        match dict:
            case {'artifact': _, 'written_content_id': _}:
                artifact = models.Artifact.objects.get(world=world, chronicle_id=dict['artifact'])
                wc = models.WrittenContents.objects.get(world=world, chronicle_id=dict['written_content_id'])
                artifact.written_content_id = wc
                artifact.save()
                if debug:
                    fkeys.remove(dict)
            # Historical event
            case {'historical_event': _, 'identity': _}:
                he = models.HistoricalEvents.objects.get(world=world, chronicle_id=dict['historical_event'])
                identity = models.Identities.objects.get(world=world, chronicle_id=dict['identity'])
                he.identity = identity
                he.save()
                if debug:
                    fkeys.remove(dict)
            case {'historical_event': _, 'target_identity': _}:
                he = models.HistoricalEvents.objects.get(world=world, chronicle_id=dict['historical_event'])
                ti = models.Identities.objects.get(world=world, chronicle_id=dict['target_identity'])
                he.target_identity = ti
                he.save()
                if debug:
                    fkeys.remove(dict)
            case {'historical_event': _, 'written_content': _}:
                he = models.HistoricalEvents.objects.get(world=world, chronicle_id=dict['historical_event'])
                wc = models.WrittenContents.objects.get(world=world, chronicle_id=dict['written_content'])
                he.written_content = wc
                he.save()
                if debug:
                    fkeys.remove(dict)
            case {'historical_event': _, 'musical_form': _}:
                he = models.HistoricalEvents.objects.get(world=world, chronicle_id=dict['historical_event'])
                mf = models.MusicalForms.objects.get(world=world, chronicle_id=dict['musical_form'])
                he.musical_form = mf
                he.save()
                if debug:
                    fkeys.remove(dict)
            case {'historical_event': _, 'poetic_form': _}:
                he = models.HistoricalEvents.objects.get(world=world, chronicle_id=dict['historical_event'])
                pf = models.PoeticForms.objects.get(world=world, chronicle_id=dict['poetic_form'])
                he.poetic_form = pf
                he.save()
                if debug:
                    fkeys.remove(dict)
            case {'historical_event': _, 'dance_form': _}:
                he = models.HistoricalEvents.objects.get(world=world, chronicle_id=dict['historical_event'])
                df = models.DanceForms.objects.get(world=world, chronicle_id=dict['dance_form'])
                he.dance_form = df
                he.save()
                if debug:
                    fkeys.remove(dict)
            # Historical figure
            case {'historical_figure': _, 'current_identity': _}:
                ...
            case {'historical_figure': _, 'used_identity': _}:
                ...
            case {'historical_figure': _, 'held_artifact': _}:
                ...
            case {'historical_figure': _, 'ent_pop_id': _}:
                ...
            case {'entity_link': _, 'civ_id': _}:
                ...
            case {'site_link': _, 'site_id': _}:
                ...
            case {'site_link': _, 'civ_id': _}:
                ...
            case {'site_link': _, 'structure': _}:
                ...
            case {'hf_link': _, 'hf_id': _}:
                ...
            case {'entity_former_position_link': _, 'position_id': _, 'civ_id': _}:
                ...
            case {'relationship_profile_visual': _, 'target_hfid': _}:
                ...
            case {'relationship_profile_visual': _, 'known_identity': _}:
                ...
            case {'intrigue_plot': _, 'civ_id': _}:
                ...
            case {'intrigue_plot': _, 'artifact': _}:
                ...
            case {'intrigue_plot': _, 'actor_id': _}:
                ...
            case {'intrigue_plot': _, 'delegated_plot_hfid': _}:
                ...
            case {'intrigue_actor': _, 'target_hfid': _}:
                ...
            case {'intrigue_actor': _, 'civ_id': _}:
                ...
            case {'entity_position_link': _, 'position_id': _}:
                ...
            case {'entity_position_link': _, 'civ_id': _}:
                ...
            case {'vague_relationship': _, 'target_hfid': _}:
                ...
            case {'entity_squad_link': _, 'civ_id': _}:
                ...
            case {'chronicle': _, 'musical': _}:
                ...
            case {'chronicle': _, 'poetic': _}:
                ...
            case {'chronicle': _, 'dance': _}:
                ...
            case _:
                open('log.txt', 'a').write(f'!MISSING VALUE! {dict}\n')