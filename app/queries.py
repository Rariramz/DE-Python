from psycopg import connect
from app.config import get_config
from app.logger import get_logger

def run_query(filepath: str):
    config = get_config()
    logger = get_logger('app.queries')

    with open(filepath, "r") as f:
        query = f.read()

    with connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            logger.info("Successfully executed queries from %s", filepath)
            return cur.fetchall()

def get_rooms_students_counts():
    return run_query('queries_sql/rooms_students_count.sql')

# TODO: move converting Decimal into reusable util
def get_rooms_w_lowest_age():
    results = run_query('queries_sql/five_rooms_lowest_age.sql')
    cleaned_results = []
    for row in results:
        room_id, room_name, avg_age = row
        avg_age = float(avg_age) if avg_age is not None else None
        cleaned_results.append((room_id, room_name, avg_age))
    return cleaned_results
    
def get_rooms_w_biggest_age_delta():
    results = run_query('queries_sql/five_rooms_biggest_age_delta.sql')
    cleaned_results = []
    for row in results:
        room_id, room_name, age_delta = row
        age_delta = float(age_delta) if age_delta is not None else None
        cleaned_results.append((room_id, room_name, age_delta))
    return cleaned_results
    
def get_multinational_rooms():
    return run_query('queries_sql/multinational_rooms.sql')