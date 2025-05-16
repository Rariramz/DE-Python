import os
import json
import xml.etree.ElementTree as ET

def export_json(data: list, filename: str):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

def export_xml(data: list[dict], root_tag: str, filename: str):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    root = ET.Element(root_tag)
    for row in data:
        item = ET.SubElement(root, "item")
        for key, val in row.items():
            child = ET.SubElement(item, key)
            child.text = str(val)
    tree = ET.ElementTree(root)
    tree.write(filename)