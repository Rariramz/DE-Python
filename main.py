import os
from app.db_init import init
from app.etl import load_rooms, load_students
import argparse
from app.queries import get_rooms_students_counts
from app.exporter import export_json, export_xml
from app.logger import get_logger

if __name__ == "__main__":
    init()
    load_rooms()
    load_students()

    parser = argparse.ArgumentParser()
    parser.add_argument("--format", choices=["json", "xml"], default="json")
    args = parser.parse_args()

    data = get_rooms_students_counts()
    structured = [{"id": r[0], "name": r[1], "count": r[2]} for r in data]

    if args.format == "json":
        export_json(structured, "exports/output.json")
    else:
        export_xml(structured, "rooms", "exports/output.xml")

