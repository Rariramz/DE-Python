from decimal import Decimal
from unittest.mock import patch

from app.queries import get_rooms_w_biggest_age_delta, get_rooms_w_lowest_age


def test_lowest_age_converts_postgres_decimal():
    with patch("app.queries.run_query", return_value=[(101, "Room A", Decimal("21.5"))]):
        result = get_rooms_w_lowest_age()

    assert result == [(101, "Room A", 21.5)]


def test_biggest_age_delta_keeps_null_and_converts_decimal():
    rows = [(101, "Room A", Decimal("4")), (102, "Room B", None)]
    with patch("app.queries.run_query", return_value=rows):
        result = get_rooms_w_biggest_age_delta()

    assert result == [(101, "Room A", 4.0), (102, "Room B", None)]
