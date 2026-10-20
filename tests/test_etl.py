from unittest.mock import MagicMock, call, patch

from app.etl import load_table


def test_load_table_inserts_every_csv_row(tmp_path):
    csv_file = tmp_path / "rooms.csv"
    csv_file.write_text("id,name\n1,Room A\n2,Room B\n", encoding="utf-8")

    connection = MagicMock()
    cursor = MagicMock()
    connection.__enter__.return_value = connection
    connection.cursor.return_value.__enter__.return_value = cursor

    with (
        patch("app.etl.get_config", return_value={"dbname": "test"}),
        patch("app.etl.psycopg.connect", return_value=connection) as connect,
    ):
        load_table(str(csv_file), "rooms")

    connect.assert_called_once_with(dbname="test")
    assert cursor.execute.call_args_list == [
        call("INSERT INTO rooms (id, name) VALUES (%s, %s)", ["1", "Room A"]),
        call("INSERT INTO rooms (id, name) VALUES (%s, %s)", ["2", "Room B"]),
    ]
    connection.commit.assert_called_once_with()
