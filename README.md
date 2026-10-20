# Student Housing Analytics

This is a small data engineering project I built to practise working with Python, PostgreSQL, and raw SQL. It loads student and room data from CSV files, runs several analytical queries in the database, and exports the results as JSON or XML.

The queries answer four questions:

- How many students live in each room?
- Which five rooms have the lowest average age?
- Which five rooms have the largest age difference?
- Which rooms contain students of different nationalities?

Sample inputs are in [`csv/`](csv/) and example results are in [`exports/`](exports/).

## Run with Docker

The quickest way to run the sample pipeline is:

```bash
docker compose up --build --abort-on-container-exit app
```

This starts PostgreSQL, creates the schema, loads the sample data, and writes JSON results to `exports/`.

To export XML instead:

```bash
docker compose run --rm app python main.py \
  --init schema/init_db.sql \
  --rooms csv/test_rooms.csv \
  --students csv/test_students.csv \
  --format xml
```

If port `5432` is already occupied, set `POSTGRES_HOST_PORT` to another port before starting Docker Compose.

## Run locally

Start PostgreSQL and install the Python dependencies:

```bash
docker compose up -d postgres
python -m venv .venv
python -m pip install -r requirements.txt
```

Then run:

```bash
python main.py \
  --init schema/init_db.sql \
  --rooms csv/test_rooms.csv \
  --students csv/test_students.csv \
  --format json
```

Connection settings are read from `config.yaml`. They can also be overridden with the standard `POSTGRES_HOST`, `POSTGRES_PORT`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, and `POSTGRES_DB` environment variables.

The expected CSV headers are:

- Rooms: `id,name`
- Students: `id,name,age,room,sex,nationality`

## Tests

```bash
python -m pip install -r requirements-dev.txt
pytest
ruff check .
```

The fast tests run without a database. GitHub Actions also runs an integration test against PostgreSQL.
