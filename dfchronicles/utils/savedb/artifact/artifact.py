def save_artifact(element, world):
    from chronicle_compiler import models
    artifact_arguments = []

    chronicle_id, name, name2, missing_site_id, missing_holder_id, page_number, missing_written_content_id, item_type, material, item_subtype, item_description, missing_structure_local_id = None, None, None, None, None, None, None, None, None, None, None, None
    for child in element:
        if child.tag == 'id':
            chronicle_id = int(child.text)
        elif child.tag == 'name':
            name = child.text
        elif child.tag == 'item':
            for subchild in child:
                if subchild.tag == 'name_string':
                    name2 = subchild.text
                elif subchild.tag == 'page_number':
                    page_number = int(subchild.text)
                elif subchild.tag == 'page_written_content_id' or subchild.tag == 'writing_written_content_id':
                    # place in missing_fkeys, WrittenContent's are not saved yet
                    missing_written_content_id = int(subchild.text)
        elif child.tag == 'site_id':
            site = models.Sites.objects.get(chronicle_id=int(child.text))
            artifact_arguments.append({'site': site})
        elif child.tag == 'holder_hfid':
            holder_hfid = models.HistoricalFigures.objects.get(world=world, chronicle_id=int(child.text))
        elif child.tag == 'item_type':
            item_type = child.text
        elif child.tag == 'mat':
            material = child.text
        elif child.tag == 'item_subtype':
            item_subtype = child.text
        elif child.tag == 'item_description':
            item_description = child.text
        elif child.tag == 'structure_local_id':
            missing_structure_local_id = int(child.text)
        elif child.tag == 'page_count' or child.tag == 'writing' or child.tag == 'abs_tile_x' or child.tag == 'abs_tile_y' or child.tag == 'abs_tile_z':
            pass
        else:
            open('log.txt', 'a').write('!UNUSED TAG! Save Artifact: ' + child.tag + '\n')
        

    try:
        artifact = models.Artifact.objects.get(world=world, chronicle_id=chronicle_id)
        exists = True
    except models.Artifact.DoesNotExist:
        exists = False

    if exists:
        # Artifact has been seen before, update it
        if item_type:
            artifact.item_type = item_type
        if material:
            artifact.material = material
        if item_subtype:
            artifact.item_subtype = item_subtype
        if item_description:
            artifact.item_description = item_description
        artifact.save()
    else:
        # Artifact has not been seen before, create it
        artifact_arguments.append({'world' : world, 'chronicle_id': chronicle_id, 'name': name, 'name2': name2, 'page_number': page_number, 'item_type': item_type, 'material': material, 'item_subtype': item_subtype, 'item_description': item_description, 'site_id': site, 'holder_id': holder_hfid})

        artifact = models.Artifact.objects.create(**artifact_arguments[0])
        artifact.save()


        missing = {'artifact': artifact}
        if missing_written_content_id:
            try:
                written_content = models.WrittenContents.objects.get(world=world, chronicle_id=missing_written_content_id)
                artifact.written_content_id = written_content
            except models.WrittenContents.DoesNotExist:
                missing['written_content_id'] = missing_written_content_id
        if missing_structure_local_id:
            try:
                structure = models.Structures.objects.get(world=world, structure_id=missing_structure_local_id, site_id=models.Sites.objects.get(world=world, chronicle_id=missing_site_id))
                artifact.structure_local_id = structure
            except models.Structures.DoesNotExist:
                missing['structure_local_id'] = missing_structure_local_id

        artifact.save()

        return missing
