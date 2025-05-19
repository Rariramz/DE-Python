import os
from app.db_init import init_db
from app.etl import load_table
import argparse
from app.queries import (
    get_rooms_students_counts,
    get_rooms_w_lowest_age,
    get_rooms_w_biggest_age_delta,
    get_multinational_rooms
)
from app.exporter import export_data
from app.logger import get_logger
from app.cli import parse_args

if __name__ == "__main__":
    args = parse_args()
    db_init_path = args.init
    students_path = args.students
    rooms_path = args.rooms
    output_format = args.format

    init_db(db_init_path)
    load_table(rooms_path, 'rooms')
    load_table(students_path, 'students')

    students_counts = get_rooms_students_counts()
    lowest_age = get_rooms_w_lowest_age()
    biggest_age_delta = get_rooms_w_biggest_age_delta()
    multinational_rooms = get_multinational_rooms()

    structured_students_counts = [{"room_id": r[0], "room_name": r[1], "students_count": r[2]} for r in students_counts]
    structured_lowest_age = [{"room_id": r[0], "room_name": r[1], "avg_age": r[2]} for r in lowest_age]
    structured_biggest_age_delta = [{"room_id": r[0], "room_name": r[1], "age_delta": r[2]} for r in biggest_age_delta]
    structured_multinational = [{"room_id": r[0], "room_name": r[1], "nationalities": r[2]} for r in multinational_rooms]

    export_data(output_format, structured_students_counts, "rooms_students_count", "rooms_students_count")
    export_data(output_format, structured_lowest_age, "rooms_lowest_age", "rooms_lowest_age")
    export_data(output_format, structured_biggest_age_delta, "rooms_biggest_age_delta", "rooms_biggest_age_delta")
    export_data(output_format, structured_multinational, "rooms_multinational", "rooms_multinational")

# python main.py --init schema/init_db.sql --students csv/students.csv --rooms csv/rooms.csv