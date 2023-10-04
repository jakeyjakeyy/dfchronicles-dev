import xml.etree.ElementTree as ET
import os

tree = ET.parse(os.path.join(os.path.dirname(__file__), 'XML', 'region3-00100-01-01-legends.xml'))
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)