FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py", "--init", "schema/init_db.sql", "--rooms", "csv/test_rooms.csv", "--students", "csv/test_students.csv", "--format", "json"]
