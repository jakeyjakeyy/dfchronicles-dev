import xml.etree.ElementTree as ET
from chronicle_compiler import models


def ParseXML(root):
    exclude_tags = ['start_seconds72', 'end_seconds72', 'birth_seconds72', 'death_seconds72', 'author_roll', 'form_id', 'coords', 'rectangle', 'world_constructions']
    exclude_redundant = ['artifact', 'entity', 'entity_population', 'historical_era', 'historical_event_collection', 'historical_event', 'historical_figure', 'region', 'site', 'underground_region', 'written_content']
    def parse_element(element):
        data = {}
        for child in element:
            if child.tag not in exclude_tags:
                if len(child) > 0:
                    if child.tag not in data:
                        data[child.tag] = []
                    data[child.tag].append(parse_element(child))
                else:
                    text = child.text
                    data[child.tag] = text
        return data

    return {root.tag: parse_element(root)}

def SaveWorld(root, owner):
    owner = models.User.objects.get(id=1)
    if root[1].tag == 'altname':
        world = models.World.objects.create(name=root[1].text, name2=root[0].text, owner=owner)
        world.save()
    return world

def SaveLegends(root, world):
    class_tags = ['artifacts', 'entities', 'entity_populations', 'historical_eras', 'historical_event_collections', 'historical_events', 'historical_figures', 'regions', 'sites', 'underground_regions', 'written_contents']
    exclude_tags = ['start_seconds72', 'end_seconds72', 'birth_seconds72', 'death_seconds72', 'author_roll', 'form_id', 'coords', 'rectangle', 'world_constructions']

    # Find all elements and run associated save function
    def save_element(element, world):
        for child in element:
            if child.tag not in exclude_tags and child.tag in class_tags:
                if child.tag == 'artifacts':
                    open('log.txt', 'a').write('Save Element: artifacts\n')
                    save_element(child, world)
                else:
                    pass
            else:
                if child.tag == 'artifact':
                    print(child.tag, open('log.txt', 'a').write('Save Element: artifact\n'))
                    save_artifact(child, world)
                else:
                    pass
    
    save_element(root, world)


    
# Save functions
def save_artifact(element, world):
    artifact_arguments = []
    missing_fkeys = []

    chronicle_id, name, name2, missing_site_id, missing_holder_id, page_number, missing_written_content_id, item_type, writing, material, item_subtype, item_description = None, None, None, None, None, None, None, None, None, None, None, None
    for child in element:
        if child.tag == 'id':
            chronicle_id = int(child.text)
        elif child.tag == 'name':
            name = child.text
        elif child.tag == 'item':
            name2 = child[0].text
        elif child.tag == 'site_id':
            # Sites should be saved at this point, so we can use the fkey
            # Commenting out for now for testing
            # site = models.Sites.objects.get(chronicle_id=int(child.text))
            # artifact_arguments.append({'site': site})

            missing_site_id = int(child.text)
        elif child.tag == 'holder_hfid':
            # place in missing_fkeys, HistoricalFigure's are not saved yet
            missing_holder_id = int(child.text)
        elif child.tag == 'page_number':
            page_number = int(child.text)
        elif child.tag == 'written_content_id':
            # place in missing_fkeys, WrittenContent's are not saved yet
            missing_written_content_id = int(child.text)
        elif child.tag == 'item_type':
            item_type = child.text
        elif child.tag == 'writing':
            writing = int(child.text)
        elif child.tag == 'mat':
            material = child.text
        elif child.tag == 'item_subtype':
            item_subtype = child.text
        elif child.tag == 'item_description':
            item_description = child.text
        else:
            open('log.txt', 'a').write('Save Artifact: !UNUSED TAG! ' + child.tag + '\n')
        
    artifact_arguments.append({'world' : world, 'chronicle_id': chronicle_id, 'name': name, 'name2': name2, 'page_number': page_number, 'item_type': item_type, 'writing': writing, 'material': material, 'item_subtype': item_subtype, 'item_description': item_description})
    artifact = models.Artifact.objects.create(**artifact_arguments[0])
    artifact.save()

    # missing_fkeys.append({'artifact': artifact, 'missing_site_id': missing_site_id, 'missing_holder_id': missing_holder_id, 'missing_written_content_id': missing_written_content_id})

