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
    return run_query('./queries_sql/rooms_students_count.sql')

def get_rooms_w_lowest_age():
    return run_query('/queries_sql/five_rooms_lowest_age.sql')
    
def get_rooms_w_biggest_age_delta():
    return run_query('/queries_sql/five_rooms_biggest_age_delta.sql')
    
def get_multinational_rooms():
    return run_query('/queries_sql/multinational_rooms.sql')