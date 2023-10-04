import xml.etree.ElementTree as ET
import os


xml = os.path.join(os.path.dirname(__file__), 'XML', 'region3-00100-01-01-legends.xml')
tree = ET.parse(xml)
root = tree.getroot()

# def parseXML(root):
#     data = {}
#     for child in root:
#         i = 0
#         data[child.tag] = {}
#         for child2 in child:
#             data[child.tag][i] = {}
#             for child3 in child2:
#                 if child3.tag != 'id':
#                     data[child.tag][i][child3.tag] = child3.text
#             i += 1
#     return data

# print(parseXML(root), file=open("output.txt","a"))


def parseXML(root):
    def parse_element(element):
        data = {}
        for i, child in enumerate(element):
            if len(child) > 0:  # Check if there are child elements
                if child.tag not in data:
                    data[child.tag] = []
                data[child.tag].append(parse_element(child))
            else:
                data[child.tag] = child.text
        return data

    return {root.tag: parse_element(root)}

print(parseXML(root), file=open("output.txt","a"))