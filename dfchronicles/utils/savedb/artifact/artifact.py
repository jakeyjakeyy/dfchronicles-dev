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
            # Sites should be saved at this point, so we can use the fkey
            # Commenting out for now for testing
            # site = models.Sites.objects.get(chronicle_id=int(child.text))
            # artifact_arguments.append({'site': site})
            missing_site_id = int(child.text)
        elif child.tag == 'holder_hfid':
            # place in missing_fkeys, HistoricalFigure's are not saved yet
            missing_holder_id = int(child.text)
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
        # artifact = models.Artifact.objects.filter(world=world, chronicle_id=chronicle_id)
        pass
    else:
        # Artifact has not been seen before, create it
        artifact_arguments.append({'world' : world, 'chronicle_id': chronicle_id, 'name': name, 'name2': name2, 'page_number': page_number, 'item_type': item_type, 'material': material, 'item_subtype': item_subtype, 'item_description': item_description})

        artifact = models.Artifact.objects.create(**artifact_arguments[0])
        artifact.save()


        missing = {'artifact': artifact}
        if missing_site_id:
            missing['site'] = missing_site_id
        if missing_holder_id:
            missing['holder_id'] = missing_holder_id
        if missing_written_content_id:
            missing['written_content_id'] = missing_written_content_id
        if missing_structure_local_id:
            missing['structure_local_id'] = missing_structure_local_id

        return missing
