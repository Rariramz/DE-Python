import os
from app.db_init import init_db
from app.etl import load_rooms, load_students
import argparse
from app.queries import get_rooms_students_counts
from app.exporter import export_json, export_xml
from app.logger import get_logger

if __name__ == "__main__":
    logger = get_logger(__name__)

    logger.info("~~~ Initializing DB... ~~")
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    init_db(os.path.join(BASE_DIR, "schema", "init_db.sql"))
    load_rooms(os.path.join(BASE_DIR, "csv", "rooms.csv"))
    load_students(os.path.join(BASE_DIR, "csv", "students.csv"))
    logger.info("~~~ DB initialized successfully! ~~")

    parser = argparse.ArgumentParser()
    parser.add_argument("--format", choices=["json", "xml"], default="json")
    args = parser.parse_args()

    logger.info("~~~ Exporting... ~~")
    data = get_rooms_students_counts()
    structured = [{"id": r[0], "name": r[1], "count": r[2]} for r in data]

    if args.format == "json":
        export_json(structured, "exports/output.json")
    else:
        export_xml(structured, "rooms", "exports/output.xml")

    logger.info("~~~ Export completed successfully! ~~")
