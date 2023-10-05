import xml.etree.ElementTree as ET


def XMLRoot(xml):
    tree = ET.parse(xml)
    root = tree.getroot()
    return root

def parseXML(root):
    def parse_element(element):
        data = {}
        for child in element:
            if child.tag != 'start_seconds72' and child.tag != 'end_seconds72' and child.tag != 'birth_seconds72' and child.tag != 'death_seconds72' and child.tag != 'author_roll' and child.tag != 'form_id' and child.tag != 'coords' and child.tag != 'rectangle' and child.tag != 'world_constructions':
                if len(child) > 0:
                    if child.tag not in data:
                        data[child.tag] = []
                    data[child.tag].append(parse_element(child))
                else:
                    text = child.text
                    if text is not None:
                        text = text.strip('"')
                        data[child.tag] = text
        return data

    return {root.tag: parse_element(root)}
# to convert to json
# parsed = parseXML(root)
# json_object = json.dumps(parsed, indent=2, sort_keys=True)

