import xml.etree.ElementTree as ET
import os


xml = os.path.join(os.path.dirname(__file__), 'XML', 'legends_sample.xml')
tree = ET.parse(xml)
root = tree.getroot()


def parseXML(root):
    def parse_element(element):
        data = {}
        for i, child in enumerate(element):
            # if child.tag != 'id':
            if child.tag != 'start_seconds72' and child.tag != 'end_seconds72':
                if len(child) > 0: 
                    if child.tag not in data:
                        data[child.tag] = []
                    data[child.tag].append(parse_element(child))
                else:
                    data[child.tag] = child.text
        return data

    return {root.tag: parse_element(root)}

parsed = parseXML(root)
print(parsed, file=open("output.txt","a"))

# print(parsed)