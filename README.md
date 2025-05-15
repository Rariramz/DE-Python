# 🐍 Python Introduction Project

## 📝 Summary

This project is a Python-based command-line tool designed to load student and room data into a relational database (MySQL or PostgreSQL), perform analytical queries, and export the results in JSON or XML format.  
It touches on several foundational concepts of DE (schema design, SQL, file parsing, Docker, CLI, testing, and more).

### 🔧 Features
- Many-to-one relational schema between students and rooms.
- Raw SQL queries (no ORM).
- Optimized with indexes.
- Query results exported in JSON or XML.
- Dockerized deployment using `docker-compose`.
- Unit tested and follows SOLID principles.

### 🛠️ Technologies
- Python 3
- MySQL or PostgreSQL
- Docker & Docker Compose
- Raw SQL
- JSON/XML data handling

---

<details>
<summary>📌 <strong>Task Details</strong> (Click to expand)</summary>

### 🎯 Objective

Design a schema using **MySQL** or **PostgreSQL** to represent a **many-to-one** relationship between students and rooms.  
Build a Python-based CLI application to:

- Load student and room data from provided files.
- Store the data into the relational database.
- Perform analytical queries and export results in **JSON** or **XML** formats.

### 📁 Input Files

The application expects two input files:

- `students`: Path to the student data file.
- `rooms`: Path to the room data file.

### 🧩 Database Schema

A relational schema should be created to represent the data, ensuring a **many-to-one** relationship (i.e., many students can belong to one room).

### 🔍 Query Requirements

1. List of rooms and the number of students in each room.
2. Five rooms with the **lowest average student age**.
3. Five rooms with the **highest age difference** among students.
4. List of rooms where students of **different nationalities** live.

All calculations **must be performed at the database level using raw SQL** (no ORM).

### 🚀 Optimization

- Propose and implement **indexing strategies** for performance.
- Provide an SQL script to create all necessary **indexes**.

### 📤 Output Formats

Support the following export formats:

- `--format json`
- `--format xml`

### 🖥️ Command-Line Interface

The script should be executable from the command line with the following parameters:

```bash
python main.py --students path/to/students.json --rooms path/to/rooms.json --format json
