import csv
import psycopg
from app.config import get_config
from app.logger import get_logger
import logging

def load_table(filepath: str, table_name: str):
    config = get_config()
    logger = get_logger("app.etl")

    logger.info("Loading csv from %s into table %s", filepath, table_name)
    with psycopg.connect(**config) as conn:
        with conn.cursor() as cur:
            with open(filepath, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                columns = reader.fieldnames
                placeholders = ', '.join(['%s'] * len(columns))
                columns_names = ', '.join(columns)
                insert_sql = f'INSERT INTO {table_name} ({columns_names}) VALUES ({placeholders})'
                for row in reader:
                    values = [row[c] for c in columns]
                    cur.execute(insert_sql, values)
        conn.commit()
    logger.info("Loaded records from csv %s into %s table successfully!", filepath, table_name)

def load_rooms():
    load_table('./csv/rooms.csv', 'rooms')

def load_students():
    load_table('./csv/students.csv', 'students')
