debug = True
def link_fkeys(fkeys, world):
    from chronicle_compiler import models
    for dict in fkeys:
        match dict:
            case {'artifact': _, 'written_content_id': _}:
                artifact = 'artifact'
                wc = models.WrittenContents.objects.get(world=world, chronicle_id=dict['written_content_id'])
                artifact.written_content_id = wc
                artifact.save()
            # Historical event
            case {'historical_event': _, 'identity': _}:
                he = 'historical_event'
                identity = models.Identities.objects.get(world=world, chronicle_id=dict['identity'])
                he.identity = identity
                he.save()
            case {'historical_event': _, 'target_identity': _}:
                he = 'historical_event'
                ti = models.Identities.objects.get(world=world, chronicle_id=dict['target_identity'])
                he.target_identity = ti
                he.save()
            case {'historical_event': _, 'written_content': _}:
                he = 'historical_event'
                wc = models.WrittenContents.objects.get(world=world, chronicle_id=dict['written_content'])
                he.written_content = wc
                he.save()
            case {'historical_event': _, 'musical_form': _}:
                he = 'historical_event'
                mf = models.MusicalForms.objects.get(world=world, chronicle_id=dict['musical_form'])
                he.musical_form = mf
                he.save()
            case {'historical_event': _, 'poetic_form': _}:
                he = 'historical_event'
                pf = models.PoeticForms.objects.get(world=world, chronicle_id=dict['poetic_form'])
                he.poetic_form = pf
                he.save()
            case {'historical_event': _, 'dance_form': _}:
                he = 'historical_event'
                df = models.DanceForms.objects.get(world=world, chronicle_id=dict['dance_form'])
                he.dance_form = df
                he.save()
            # Historical figure
            case {'historical_figure': _, 'current_identity': _}:
                hf = 'historical_figure'
                ci = models.Identities.objects.get(world=world, chronicle_id=dict['current_identity'])
                hf.current_identity = ci
                hf.save()
            case {'historical_figure': _, 'used_identity': _}:
                hf = 'historical_figure'
                ui = models.Identities.objects.get(world=world, chronicle_id=dict['used_identity'])
                hf.used_identity = ui
                hf.save()
            case {'historical_figure': _, 'held_artifact': _}:
                hf = 'historical_figure'
                ha = models.Artifact.objects.get(world=world, chronicle_id=dict['held_artifact'])
                hf.held_artifact = ha
                hf.save()
            case {'historical_figure': _, 'ent_pop_id': _}:
                hf = 'historical_figure'
                ep = models.Entities.objects.get(world=world, chronicle_id=dict['ent_pop_id'])
                hf.ent_pop_id = ep
                hf.save()
            case {'entity_link': _, 'civ_id': _}:
                el = 'entity_link'
                civ = models.Entities.objects.get(world=world, chronicle_id=dict['civ_id'])
                el.civ_id = civ
                el.save()
            case {'site_link': _, 'site_id': _}:
                sl = 'site_link'
                site = models.Sites.objects.get(world=world, chronicle_id=dict['site_id'])
                sl.site_id = site
                sl.save()
            case {'site_link': _, 'civ_id': _}:
                sl = 'site_link'
                civ = models.Entities.objects.get(world=world, chronicle_id=dict['civ_id'])
                sl.civ_id = civ
                sl.save()
            case {'site_link': _, 'structure': _}:
                sl = 'site_link'
                structure = models.Structures.objects.get(world=world, chronicle_id=dict['structure'])
                sl.structure = structure
                sl.save()
            case {'hf_link': _, 'hf_id': _}:
                hfl = 'hf_link'
                hf = models.HistoricalFigures.objects.get(world=world, chronicle_id=dict['hf_id'])
                hfl.hf_id = hf
            case {'entity_former_position_link': _, 'position_id': _, 'civ_id': _}:
                fpl = 'entity_former_position_link'
                position = models.Positions.objects.get(world=world, civ_position_id=dict['position_id'], civ_id=dict['civ_id'])
                fpl.position_id = position
                fpl.save()
            case {'relationship_profile_visual': _, 'target_hfid': _}:
                rpv = 'relationship_profile_visual'
                hf = models.HistoricalFigures.objects.get(world=world, chronicle_id=dict['target_hfid'])
                rpv.target_hfid = hf
                rpv.save()
            case {'relationship_profile_visual': _, 'known_identity': _}:
                rpv = 'relationship_profile_visual'
                identity = models.Identities.objects.get(world=world, chronicle_id=dict['known_identity'])
                rpv.known_identity = identity
                rpv.save()
            case {'intrigue_plot': _, 'civ_id': _}:
                ip = 'intrigue_plot'
                civ = models.Entities.objects.get(world=world, chronicle_id=dict['civ_id'])
                ip.civ_id = civ
                ip.save()
            case {'intrigue_plot': _, 'artifact': _}:
                ip = 'intrigue_plot'
                artifact = models.Artifact.objects.get(world=world, chronicle_id=dict['artifact'])
                ip.artifact = artifact
                ip.save()
            case {'intrigue_plot': _, 'actor_id': _}:
                ip = 'intrigue_plot'
                actor = models.HistoricalFigures.objects.get(world=world, chronicle_id=dict['actor_id'])
                ip.actor_id = actor
                ip.save()
            case {'intrigue_plot': _, 'delegated_plot_hfid': _}:
                ip = 'intrigue_plot'
                delegated_plot_hfid = models.HistoricalFigures.objects.get(world=world, chronicle_id=dict['delegated_plot_hfid'])
                ip.delegated_plot_hfid = delegated_plot_hfid
                ip.save()
            case {'intrigue_actor': _, 'target_hfid': _}:
                ia = 'intrigue_actor'
                target_hfid = models.HistoricalFigures.objects.get(world=world, chronicle_id=dict['target_hfid'])
                ia.target_hfid = target_hfid
                ia.save()
            case {'intrigue_actor': _, 'civ_id': _}:
                ia = 'intrigue_actor'
                civ = models.Entities.objects.get(world=world, chronicle_id=dict['civ_id'])
                ia.civ_id = civ
                ia.save()
            case {'entity_position_link': _, 'position_id': _, 'civ_id': _}:
                epl = 'entity_position_link'
                position = models.Positions.objects.get(world=world, civ_position_id=dict['position_id'], civ_id=dict['civ_id'])
                epl.position_id = position
                epl.save()
            case {'entity_position_link': _, 'civ_id': _}:
                epl = 'entity_position_link'
                civ = models.Entities.objects.get(world=world, chronicle_id=dict['civ_id'])
                epl.civ_id = civ
                epl.save()
            case {'vague_relationship': _, 'target_hfid': _}:
                vr = 'vague_relationship'
                target_hfid = models.HistoricalFigures.objects.get(world=world, chronicle_id=dict['target_hfid'])
                vr.target_hfid = target_hfid
                vr.save()
            case {'entity_squad_link': _, 'civ_id': _}:
                esl = 'entity_squad_link'
                civ = models.Entities.objects.get(world=world, chronicle_id=dict['civ_id'])
                esl.civ_id = civ
                esl.save()
            case {'chronicle': _, 'musical': _}:
                chronicle = 'chronicle'
                musical = models.MusicalForms.objects.get(world=world, chronicle_id=dict['musical'])
                wcf = models.WrittenContentReference.objects.create(world=world, written_content=chronicle, musical_form=musical)
                wcf.save()
            case {'chronicle': _, 'poetic': _}:
                chronicle = 'chronicle'
                poetic = models.PoeticForms.objects.get(world=world, chronicle_id=dict['poetic'])
                wcf = models.WrittenContentReference.objects.create(world=world, written_content=chronicle, poetic_form=poetic)
                wcf.save()
            case {'chronicle': _, 'dance': _}:
                chronicle = 'chronicle'
                dance = models.DanceForms.objects.get(world=world, chronicle_id=dict['dance'])
                wcf = models.WrittenContentReference.objects.create(world=world, written_content=chronicle, dance_form=dance)
                wcf.save()
            case {'chronicle': _, 'site': _}:
                chronicle = 'chronicle'
                site = models.Sites.objects.get(world=world, chronicle_id=dict['site'])
                wcf = models.WrittenContentReference.objects.create(world=world, written_content=chronicle, site=site)
                wcf.save()
            case {'chronicle': _, 'written_content': _}:
                chronicle = 'chronicle'
                written_content = models.WrittenContents.objects.get(world=world, chronicle_id=dict['written_content'])
                wcf = models.WrittenContentReference.objects.create(world=world, written_content=chronicle, written_content=written_content)
                wcf.save()
            case _:
                open('log.txt', 'a').write(f'!MISSING VALUE! {dict}\n')
        
        if debug:
            fkeys.remove(dict)