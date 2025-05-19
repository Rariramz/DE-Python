import os
from psycopg import connect
from app.config import get_config
from app.logger import get_logger

def init_db(pathname: str):
    config = get_config()
    logger = get_logger('app.db_init')
    
    with open(pathname, 'r') as f:
        sql = f.read()
    
    with connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
        conn.commit()
    logger.info('Successfully initialized DB with sql from %s', pathname)
