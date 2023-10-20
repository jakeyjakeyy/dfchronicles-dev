debug = True
def link_fkeys(fkeys, world):
    from chronicle_compiler import models
    for dict in fkeys:
        match dict:
            case {'artifact': _, 'written_content_id': _}:
                artifact = models.Artifact.objects.get(id=dict['artifact'])
                wc = models.WrittenContents.objects.get(world=world, chronicle_id=dict['written_content_id'])
                artifact.written_content_id = wc
                artifact.save()
            # Historical event
            case {'historical_event': _, 'identity': _}:
                he = models.HistoricalEvents.objects.get(id=dict['historical_event'])
                try:
                    identity = models.Identities.objects.get(world=world, chronicle_id=dict['identity'])
                except models.Identities.DoesNotExist:
                    with open('log.txt', 'a') as log:
                        log.write(f'!PROBLEM CHILD >:(! {dict}\n')
                he.identity = identity
                he.save()
            case {'historical_event': _, 'target_identity': _}:
                he = models.HistoricalEvents.objects.get(id=dict['historical_event'])
                ti = models.Identities.objects.get(world=world, chronicle_id=dict['target_identity'])
                he.target_identity = ti
                he.save()
            case {'historical_event': _, 'written_content': _}:
                he = models.HistoricalEvents.objects.get(id=dict['historical_event'])
                wc = models.WrittenContents.objects.get(world=world, chronicle_id=dict['written_content'])
                he.written_content = wc
                he.save()
            case {'historical_event': _, 'musical_form': _}:
                he = models.HistoricalEvents.objects.get(id=dict['historical_event'])
                mf = models.MusicalForms.objects.get(world=world, chronicle_id=dict['musical_form'])
                he.musical_form = mf
                he.save()
            case {'historical_event': _, 'poetic_form': _}:
                he = models.HistoricalEvents.objects.get(id=dict['historical_event'])
                pf = models.PoeticForms.objects.get(world=world, chronicle_id=dict['poetic_form'])
                he.poetic_form = pf
                he.save()
            case {'historical_event': _, 'dance_form': _}:
                he = models.HistoricalEvents.objects.get(id=dict['historical_event'])
                df = models.DanceForms.objects.get(world=world, chronicle_id=dict['dance_form'])
                he.dance_form = df
                he.save()
            case {'historical_event': _, 'position_id': _, 'civ_id': _}:
                he = models.HistoricalEvents.objects.get(id=dict['historical_event'])
                civ = models.Entities.objects.get(world=world, chronicle_id=dict['civ_id'])
                try:
                    position = models.EntityPosition.objects.get(world=world, civ_position_id=dict['position_id'], civ_id=civ)
                except models.EntityPosition.DoesNotExist:
                    with open('log.txt', 'a') as log:
                        log.write(f'!PROBLEM CHILD >:(! {dict}\n')
                he.position_id = position
                he.save()
            case {'historical_event': _, 'occasion': _, 'civ_id': _}:
                he = models.HistoricalEvents.objects.get(id=dict['historical_event'])
                civ = models.Entities.objects.get(world=world, chronicle_id=dict['civ_id'])
                occasion = models.Occasions.objects.get(world=world, civ_occasion_id=dict['occasion'], civ_id=civ)
                he.occasion = occasion
                he.save()
            case {'historical_event': _, 'schedule': _, 'occasion': _}:
                he = models.HistoricalEvents.objects.get(id=dict['historical_event'])
                civ = models.Entities.objects.get(world=world, chronicle_id=dict['civ_id'])
                occasion = models.Occasions.objects.get(world=world, civ_occasion_id=dict['occasion'], civ_id=civ)
                schedule = models.Schedules.objects.get(world=world, occasion_schedule_id=dict['schedule'], occasion=occasion)
            # Historical figure
            case {'historicfigure': _, 'current_identity': _}:
                hf = models.HistoricalFigures.objects.get(id=dict['historicfigure'])
                ci = models.Identities.objects.get(world=world, chronicle_id=dict['current_identity'])
                hf.current_identity = ci
                hf.save()
            case {'historicfigure': _, 'used_identity': _}:
                hf = models.HistoricalFigures.objects.get(id=dict['historicfigure'])
                ui = models.Identities.objects.get(world=world, chronicle_id=dict['used_identity'])
                hf.used_identity.add(ui)
                hf.save()
            case {'historicfigure': _, 'held_artifact': _}:
                hf = models.HistoricalFigures.objects.get(id=dict['historicfigure'])
                ha = models.Artifact.objects.get(world=world, chronicle_id=dict['held_artifact'])
                hf.held_artifact.add(ha)
                hf.save()
            case {'historicfigure': _, 'ent_pop_id': _}:
                hf = models.HistoricalFigures.objects.get(id=dict['historicfigure'])
                ep = models.EntityPopulations.objects.get(world=world, chronicle_id=dict['ent_pop_id'])
                hf.ent_pop_id = ep
                hf.save()
            case {'entity_link': _, 'civ_id': _}:
                el = models.EntityLink.objects.get(id=dict['entity_link'])
                civ = models.Entities.objects.get(world=world, chronicle_id=dict['civ_id'])
                el.civ_id = civ
                el.save()
            case {'site_link': _, 'site_id': _}:
                sl = models.SiteLink.objects.get(id=dict['site_link'])
                site = models.Sites.objects.get(world=world, chronicle_id=dict['site_id'])
                sl.site_id = site
                sl.save()
            case {'site_link': _, 'civ_id': _}:
                sl = models.SiteLink.objects.get(id=dict['site_link'])
                civ = models.Entities.objects.get(world=world, chronicle_id=dict['civ_id'])
                sl.civ_id = civ
                sl.save()
            case {'site_link': _, 'structure': _, 'site': _}:
                sl = models.SiteLink.objects.get(id=dict['site_link'])
                structure = models.Structures.objects.get(world=world, structure_id=dict['structure'], site_id=models.Sites.objects.get(world=world, chronicle_id=dict['site']))
                sl.structure = structure
                sl.save()
            case {'hf_link': _, 'hf_id': _}:
                hfl = models.HfLink.objects.get(id=dict['hf_link'])
                hf = models.HistoricalFigures.objects.get(world=world, chronicle_id=dict['hf_id'])
                hfl.hf_id = hf
            case {'entity_former_position_link': _, 'position_id': _, 'civ_id': _}:
                fpl = models.EntityFormerPositionLink.objects.get(id=dict['entity_former_position_link'])
                civ = models.Entities.objects.get(world=world, chronicle_id=dict['civ_id'])
                try:
                    position = models.EntityPosition.objects.get(world=world, civ_position_id=int(dict['position_id']), civ_id=civ)
                except models.EntityPosition.DoesNotExist:
                    with open('log.txt', 'a') as log:
                        log.write(f'!PROBLEM CHILD >:(! {dict}\n')
                fpl.position_id = position
                fpl.civ_id = civ
                fpl.save()
            case {'relationship_profile_visual': _, 'target_hfid': _}:
                rpv = models.RelationshipProfileVisual.objects.get(id=dict['relationship_profile_visual'])
                hf = models.HistoricalFigures.objects.get(world=world, chronicle_id=dict['target_hfid'])
                rpv.target_hfid = hf
                rpv.save()
            case {'relationship_profile_visual': _, 'known_identity': _}:
                rpv = models.RelationshipProfileVisual.objects.get(id=dict['relationship_profile_visual'])
                try:
                    identity = models.Identities.objects.get(world=world, chronicle_id=dict['known_identity'])
                except models.Identities.DoesNotExist:
                    with open('log.txt', 'a') as log:
                        log.write(f'!PROBLEM CHILD >:(! {dict}\n')
                rpv.known_identity = identity
                rpv.save()
            case {'intrigue_plot': _, 'civ_id': _}:
                ip = models.IntriguePlot.objects.get(id=dict['intrigue_plot'])
                civ = models.Entities.objects.get(world=world, chronicle_id=dict['civ_id'])
                ip.civ_id = civ
                ip.save()
            case {'intrigue_plot': _, 'artifact': _}:
                ip = models.IntriguePlot.objects.get(id=dict['intrigue_plot'])
                artifact = models.Artifact.objects.get(world=world, chronicle_id=dict['artifact'])
                ip.artifact = artifact
                ip.save()
            case {'intrigue_plot': _, 'actor_id': _}:
                ip = models.IntriguePlot.objects.get(id=dict['intrigue_plot'])
                actor = models.HistoricalFigures.objects.get(world=world, chronicle_id=dict['actor_id'])
                ip.actor_id = actor
                ip.save()
            case {'intrigue_plot': _, 'delegated_plot_hfid': _}:
                ip = models.IntriguePlot.objects.get(id=dict['intrigue_plot'])
                delegated_plot_hfid = models.HistoricalFigures.objects.get(world=world, chronicle_id=dict['delegated_plot_hfid'])
                ip.delegated_plot_hfid = delegated_plot_hfid
                ip.save()
            case {'intrigue_actor': _, 'target_hfid': _}:
                ia = models.IntrigueActor.objects.get(id=dict['intrigue_actor'])
                target_hfid = models.HistoricalFigures.objects.get(world=world, chronicle_id=dict['target_hfid'])
                ia.target_hfid = target_hfid
                ia.save()
            case {'intrigue_actor': _, 'civ_id': _}:
                ia = models.IntrigueActor.objects.get(id=dict['intrigue_actor'])
                civ = models.Entities.objects.get(world=world, chronicle_id=dict['civ_id'])
                ia.civ_id = civ
                ia.save()
            case {'entity_position_link': _, 'position_id': _, 'civ_id': _}:
                epl = models.EntityPositionLink.objects.get(id=dict['entity_position_link'])
                try:
                    position = models.EntityPosition.objects.get(world=world, civ_position_id=dict['position_id'], civ_id=models.Entities.objects.get(world=world, chronicle_id=dict['civ_id']))
                except models.EntityPosition.DoesNotExist:
                    with open('log.txt', 'a') as log:
                        log.write(f'!PROBLEM CHILD >:(! {dict}\n')
                epl.position_id = position
                epl.save()
            case {'entity_position_link': _, 'civ_id': _}:
                epl = models.EntityPositionLink.objects.get(id=dict['entity_position_link'])
                civ = models.Entities.objects.get(world=world, chronicle_id=dict['civ_id'])
                epl.civ_id = civ
                epl.save()
            case {'vague_relationship': _, 'target_hfid': _}:
                vr = models.VagueRelationship.objects.get(id=dict['vague_relationship'])
                target_hfid = models.HistoricalFigures.objects.get(world=world, chronicle_id=dict['target_hfid'])
                vr.target_hfid = target_hfid
                vr.save()
            case {'entity_squad_link': _, 'civ_id': _}:
                esl = models.EntitySquadLink.objects.get(id=dict['entity_squad_link'])
                civ = models.Entities.objects.get(world=world, chronicle_id=dict['civ_id'])
                esl.civ_id = civ
                esl.save()
            case {'chronicle': _, 'musical': _}:
                chronicle = models.WrittenContents.objects.get(id=dict['chronicle'])
                musical = models.MusicalForms.objects.get(world=world, chronicle_id=dict['musical'])
                wcf = models.WrittenContentReference.objects.create(world=world, written_content=chronicle, musical_form=musical)
                wcf.save()
            case {'chronicle': _, 'poetic': _}:
                chronicle = models.WrittenContents.objects.get(id=dict['chronicle'])
                poetic = models.PoeticForms.objects.get(world=world, chronicle_id=dict['poetic'])
                wcf = models.WrittenContentReference.objects.create(world=world, written_content=chronicle, poetic_form=poetic)
                wcf.save()
            case {'chronicle': _, 'dance': _}:
                chronicle = models.WrittenContents.objects.get(id=dict['chronicle'])
                dance = models.DanceForms.objects.get(world=world, chronicle_id=dict['dance'])
                wcf = models.WrittenContentReference.objects.create(world=world, written_content=chronicle, dance_form=dance)
                wcf.save()
            case {'chronicle': _, 'site': _}:
                chronicle = models.WrittenContents.objects.get(id=dict['chronicle'])
                site = models.Sites.objects.get(world=world, chronicle_id=dict['site'])
                wcf = models.WrittenContentReference.objects.create(world=world, written_content=chronicle, site=site)
                wcf.save()
            case {'chronicle': _, 'written_content': _}:
                chronicle = models.WrittenContents.objects.get(id=dict['chronicle'])
                written_content = models.WrittenContents.objects.get(world=world, chronicle_id=dict['written_content'])
                wcf = models.WrittenContentReference.objects.create(world=world, written_content=chronicle, written_content_reference=written_content)
                wcf.save()
            case {'plot_actor': _, 'actor_id': _}:
                # not sure how to link actor id to histfig
                pass
            case {'plot_actor': _, 'delegated_hfid': _}:
                pass
            case _:
                with open('log.txt', 'a') as log:
                    log.write(f'!MISSING VALUE! {dict}\n')
        

    if debug:
        with open('log.txt', 'a') as log:
            log.write(f'{fkeys}\n')