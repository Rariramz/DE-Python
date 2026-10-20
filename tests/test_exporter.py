import json
import xml.etree.ElementTree as ET

from app.exporter import export_json, export_xml


def test_export_json_preserves_unicode(tmp_path):
    output = tmp_path / "result.json"
    data = [{"room": "Müller Hall"}]

    export_json(data, str(output))

    assert json.loads(output.read_text(encoding="utf-8")) == data
    assert "Müller" in output.read_text(encoding="utf-8")


def test_export_xml_creates_expected_document(tmp_path):
    output = tmp_path / "result.xml"

    export_xml([{"room_id": 101, "name": "Room A"}], "rooms", str(output))

    root = ET.parse(output).getroot()
    assert root.tag == "rooms"
    assert root.findtext("item/room_id") == "101"
    assert root.findtext("item/name") == "Room A"
