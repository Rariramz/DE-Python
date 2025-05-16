import os
from psycopg import connect
from app.config import get_config

def init_db(pathname: str):
    config = get_config()
    
    with open(pathname, 'r') as f:
        sql = f.read()
    
    with connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
        conn.commit()
