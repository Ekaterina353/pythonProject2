import pytest
from src.decorators import log
import os
from typing import Iterable


@log()
def add(x, y):
    return x + y


@log(filename="test.log")
def multiply(x, y):
    return x * y


@log()
def divide(x, y):
    return x / y


@log(filename="test.log")
def explode():
    raise ValueError("Kaboom!")


def test_log_to_console(capsys):
    result = add(2, 3)
    captured = capsys.readouterr()
    assert "add ok. Result: 5" in captured.out
    assert result == 5


def test_log_to_file():
    result = multiply(2, 3)
    with open("test.log", "r") as f:
        log_content = f.read()
    assert "multiply ok. Result: 6" in log_content
    assert result == 6
    os.remove("test.log")


def test_log_exception_to_console(capsys):
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError. Inputs: (1, 0), {}" in captured.out


def test_log_exception_to_file():
    with pytest.raises(ValueError):
        explode()
    with open("test.log", "r") as f:
        log_content = f.read()
    assert "explode error: ValueError. Inputs: (), {}" in log_content
    os.remove("test.log")


# generators.py
def card_number_generator(start: int, end: int) -> str:
    """Generate card numbers in the format '0000 0000 0000 XXXX'"""
    for i in range(start, end + 1):
        yield f"0000 0000 0000 {i:04d}"


def filter_by_currency(transactions: Iterable[dict], currency_code: str) -> Iterable[dict]:
    """Filters transactions by currency code."""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions: Iterable[dict]) -> Iterable[str]:
    """Extracts descriptions from a list of transaction dictionaries."""
    for transaction in transactions:
        yield transaction.get("description")
