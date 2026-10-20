import os

import pytest

from app.db_init import init_db
from app.etl import load_table
from app.queries import (
    get_multinational_rooms,
    get_rooms_students_counts,
    get_rooms_w_biggest_age_delta,
    get_rooms_w_lowest_age,
)

pytestmark = [
    pytest.mark.integration,
    pytest.mark.skipif(
        os.getenv("RUN_INTEGRATION") != "1",
        reason="set RUN_INTEGRATION=1 with PostgreSQL running to execute",
    ),
]


@pytest.fixture(scope="module", autouse=True)
def populated_database():
    init_db("schema/init_db.sql")
    load_table("csv/test_rooms.csv", "rooms")
    load_table("csv/test_students.csv", "students")


def test_analytical_queries_end_to_end():
    counts = get_rooms_students_counts()
    lowest_age = get_rooms_w_lowest_age()
    biggest_delta = get_rooms_w_biggest_age_delta()
    multinational = get_multinational_rooms()

    assert counts == [
        (room_id, f"Room {letter}", 2) for room_id, letter in zip(range(101, 111), "ABCDEFGHIJ")
    ]
    assert lowest_age == [
        (108, "Room H", 20.5),
        (110, "Room J", 20.5),
        (101, "Room A", 21.5),
        (103, "Room C", 21.5),
        (104, "Room D", 21.5),
    ]
    assert biggest_delta == [
        (103, "Room C", 3.0),
        (102, "Room B", 2.0),
        (101, "Room A", 1.0),
        (104, "Room D", 1.0),
        (108, "Room H", 1.0),
    ]
    assert len(multinational) == 10
    assert multinational[0] == (101, "Room A", "Canada, USA")
