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


parsed = parseXML(root)
json_object = json.dumps(parsed, indent=2, sort_keys=True)

print(json_object, file=open("output.txt","a"))


# csv_headers = ['id', 'parent', 'name', 'type', 'depth']

# # Create a list to store the data
# data_dict = {}

# # Iterate through the regions in the XML and extract the data
# for region in root.find('regions').iter('region'):
#     region_id = region.find('id').text
#     data_dict[region_id] = {
#         'id': region.find('id').text,
#         'parent': region.tag,
#         'name': region.find('name').text,
#         'type': region.find('type').text,
#     }
    

# # Iterate through the underground regions in the XML and extract the data
# for underground_region in root.find('underground_regions').iter('underground_region'):
#     underground_region_id = underground_region.find('id').text
#     data_dict[underground_region_id] = {
#         'id': underground_region.find('id').text,
#         'parent': underground_region.tag,
#         'type': underground_region.find('type').text,
#         'depth': underground_region.find('depth').text,
#     }

# # Write the data to a CSV file
# with open('output.csv', 'w', newline='') as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow(csv_headers)
#     csv_writer.writerows(data_dict.items())
