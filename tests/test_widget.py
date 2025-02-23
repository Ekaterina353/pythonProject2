import unittest
from src.widget import mask_account_card, get_date
import pytest


@pytest.mark.parametrize("input_string, expected_output", [
    ("Счет 12345678901234567890", "Счет **7890"),
    ("Счет 40817810097658072809", "Счет **2809"),
])
def test_mask_account_card_account(input_string, expected_output):
    """Тест маскировки номера счета."""
    assert mask_account_card(input_string) == expected_output


@pytest.mark.parametrize("input_string, expected_output", [
    ("Visa 1234567890123456", "Visa 1234 56** **** 3456"),
    ("MasterCard 5555444433332222", "MasterCard 5555 44** **** 2222"),
    ("Maestro 6789012345678901", "Maestro 6789 01** **** 8901"),
    ("МИР 2202203663187272", "МИР 2202 20** **** 7272"),
    ("Visa Gold 4276950555349551", "Visa Gold 4276 95** **** 9551")
])
def test_mask_account_card_card(input_string, expected_output):
    """Тест маскировки номера карты."""
    assert mask_account_card(input_string) == expected_output


@pytest.mark.parametrize("input_date, expected_output", [
    ("2019-08-26T10:50:17.248205", "26.08.2019"),
    ("2018-07-03T06:17:20.584272", "03.07.2018"),
    ("2020-01-01T00:00:00.000000", "01.01.2020"),
])
def test_get_date_valid_date(input_date, expected_output):
    """Тест преобразования корректной даты."""
    assert get_date(input_date) == expected_output


@pytest.mark.parametrize("input_date, expected_output", [
    ("2023-12-31T23:59:59.999999", "31.12.2023"),  # Граничный случай: конец года
    ("2024-01-01T00:00:00.000000", "01.01.2024"),  # Граничный случай: начало года
    ("1970-01-01T00:00:00.000000", "01.01.1970"),  # Unix epoch
    # ("2023-10-26","26.10.2023"),# Нестанд. строка без врем.-Раском-ть когда будет реализ-а обработка  только даты
])
def test_get_date_edge_cases(input_date, expected_output):
    """Тест граничных случаев и нестандартных форматов даты."""
    assert get_date(input_date) == expected_output
