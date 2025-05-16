import csv
import psycopg
from app.config import get_config

def load_rooms(filepath: str):
    config = get_config()
    # psycopg.connect accepts a connection string or kwargs
    with psycopg.connect(**config) as conn:
        with conn.cursor() as cursor:
            with open(filepath, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    cursor.execute(
                        "INSERT INTO rooms (id, name) VALUES (%s, %s)",
                        (row['id'], row['name'])
                    )
        conn.commit()

def load_students(filepath: str):
    config = get_config()
    # psycopg.connect accepts a connection string or kwargs
    with psycopg.connect(**config) as conn:
        with conn.cursor() as cursor:
            with open(filepath, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    cursor.execute(
                        "INSERT INTO students (id, name, age, room, sex, nationality) VALUES (%s, %s, %s, %s, %s, %s)",
                        (row['id'], row['name'], row['age'], row['room'], row['sex'], row['nationality'])
                    )
        conn.commit()
