import xml.etree.ElementTree as ET
import os
import json
import pandas as pd


xml = os.path.join(os.path.dirname(__file__), 'XML', 'legends_sample.xml')
tree = ET.parse(xml)
root = tree.getroot()


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

def flatten_json(y):
    out = {}

    def flatten(x, name=""):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + "_")
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + "_")
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


parsed = parseXML(root)
parsed = flatten_json(parsed)

# print(parsed, file=open("output.txt","a"))
# print(json.dumps(parsed, indent=2, sort_keys=True), file=open("output.txt","a"))

df = pd.DataFrame([parsed])
df.to_csv('output.csv', index=False)
