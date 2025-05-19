import os
import json
import xml.etree.ElementTree as ET
from app.logger import get_logger
from typing import Union, List, Dict, Any, Optional

logger = get_logger('app.exporter')

def export_data(
    format: str,
    data: Union[List[Dict[str, Any]], Dict[str, Any]],
    filename: str,
    root_tag: Optional[str] = None
):
    if format == "json":
        export_json(data, f"exports/{filename}.json")
    else:
        export_xml(data, root_tag or filename, f"exports/{filename}.xml")

def export_json(data: list, filename: str):
    logger.info("Exporting results in json...")
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    

def export_xml(data: list[dict], root_tag: str, filename: str):
    logger.info("Exporting results in xml...")
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    root = ET.Element(root_tag)
    for row in data:
        item = ET.SubElement(root, "item")
        logger.error("ROW", row)
        for key, val in row.items():
            child = ET.SubElement(item, key)
            child.text = str(val)
    tree = ET.ElementTree(root)
    tree.write(filename)
    logger.info("Successfully exported results in xml to /exports folder")