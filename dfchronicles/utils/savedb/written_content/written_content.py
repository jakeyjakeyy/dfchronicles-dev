def save_written_content(element, world):
    from chronicle_compiler import models
    chronicle_id, author_hfid, form, title, reference = None, None, None, None, None

    styles = []

    for child in element:
        tag = child.tag.strip()
        if tag == 'id':
            chronicle_id = child.text
        elif tag == 'author_hfid':
            author_hfid = models.HistoricalFigures.objects.get(
                world=world, chronicle_id=child.text)
        elif tag == 'form':
            form = child.text
        elif tag == 'title':
            title = child.text
        elif tag == 'style':
            styles.append(child.text)
        elif tag == 'form_id':
            reference = child.text
        elif tag == 'reference':
            for sc in child:
                if sc.tag == 'SITE':
                    form = 'site'
                if sc.tag == 'WRITTEN_CONTENT':
                    form = 'written_content'
                if sc.tag == 'id':
                    reference = sc.text
        elif tag in ['author_roll', 'page_start', 'page_end', 'type', 'author',]:
            pass
        else:
            open('log.txt', 'a').write('!UNUSED CHILD! written_content: ' + tag + '\n')

    try:
        chronicle = models.WrittenContents.objects.get(
            world=world, chronicle_id=chronicle_id)
        if reference:
            if form == 'site':
                ref = models.WrittenContentReference.objects.create(world=world, written_content=chronicle, site=models.Site.objects.get(world=world, site_id=reference))
                ref.save()
            else:
                open('log.txt', 'a').write('!UNUSED CHILD! written_content_reference: ' + form + '\n')

    except models.WrittenContents.DoesNotExist:
        chronicle = models.WrittenContents.objects.create(
            world=world, chronicle_id=chronicle_id, author_hfid=author_hfid,
            form=form, title=title)
        
        if styles:
            style = (', ').join(styles)
            chronicle.style = style

        chronicle.save()

        missing_fkeys = []

        if reference:
            if form == 'musical composition':
                missing_fkeys.append({'chronicle': chronicle, 'musical': reference})
            elif form == 'poem':
                missing_fkeys.append({'chronicle': chronicle, 'poetic':reference})
            elif form == 'choreography':
                missing_fkeys.append({'chronicle': chronicle, 'dance': reference})
            elif form == 'site':
                missing_fkeys.append({'chronicle': chronicle, 'site': reference})
            elif form == 'written_content':
                missing_fkeys.append({'chronicle': chronicle, 'written_content': reference})
            else:
                open('log.txt', 'a').write('!UNUSED CHILD! written_content_reference: ' + form + '\n')
            
        return missing_fkeys