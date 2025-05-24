import pytest
from app.db_init import init_db
from app.etl import load_table
from app.queries import (
    get_rooms_students_counts,
    get_rooms_w_biggest_age_delta,
    get_rooms_w_lowest_age,
    get_multinational_rooms
)
from app.config import get_config

@pytest.fixture(scope="module", autouse=True)
def setup_test_db():
     """Init the test DB and load test data once before all tests"""
     init_db("schema/init_db.sql")
     load_table("csv/test_rooms.csv", "rooms")
     load_table("csv/test_students.csv", "students")
     yield

def test_get_rooms_studetns_counts():
    result = get_rooms_students_counts()
    assert isinstance(result, list)
    assert all(len(r) == 3 for r in result) # room_id, room_name, count

def test_get_rooms_w_lowest_age():
    result = get_rooms_w_lowest_age()
    assert isinstance(result, list)
    assert all(isinstance(r[2], float) for r in result)

def test_get_rooms_w_biggest_age_delta():
    result = get_rooms_w_biggest_age_delta()
    assert isinstance(result, list)
    assert all(isinstance(r[2], float) for r in result)

def test_get_multinational_rooms():
    result = get_multinational_rooms()
    assert isinstance(result, list)
    assert all(isinstance(r[2], str) for r in result)