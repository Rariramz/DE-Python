import os
import json
import xml.etree.ElementTree as ET
from app.logger import get_logger

logger = get_logger('app.exporter')

def export_json(data: list, filename: str):
    logger.info("Exporting results in json...")
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    logger.info("Successfully exported results in json to /exports folder")

def export_xml(data: list[dict], root_tag: str, filename: str):
    logger.info("Exporting results in xml...")
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    root = ET.Element(root_tag)
    for row in data:
        item = ET.SubElement(root, "item")
        for key, val in row.items():
            child = ET.SubElement(item, key)
            child.text = str(val)
    tree = ET.ElementTree(root)
    tree.write(filename)
    logger.info("Successfully exported results in xml to /exports folder")