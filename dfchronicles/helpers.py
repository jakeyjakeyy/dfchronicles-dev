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

       
