import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from typing import Iterable


@pytest.fixture
def sample_transactions():
    return [
        {'id': 1, 'amount': 100, 'currency': 'USD', 'description': 'Перевод средств'},
        {'id': 2, 'amount': 200, 'currency': 'EUR', 'description': 'Оплата услуг'},
        {'id': 3, 'amount': 300, 'currency': 'USD', 'description': 'Покупка товаров'},
        {'id': 4, 'amount': 400, 'currency': 'RUB', 'description': 'Перевод на карту'},
    ]


@pytest.mark.parametrize(
    "transactions, currency_code, expected",
    [
        # Тест с пустым списком транзакций
        ([], "USD", []),
        # Тест с одной транзакцией, которая совпадает по валюте
        (
                [{"operationAmount": {"currency": {"code": "USD"}}}],
                "USD",
                [{"operationAmount": {"currency": {"code": "USD"}}}],
        ),
        # Тест с одной транзакцией, которая не совпадает по валюте
        ([{"operationAmount": {"currency": {"code": "EUR"}}}], "USD", []),
        # Тест с несколькими транзакциями, из которых одна совпадает по валюте
        (
                [
                    {"operationAmount": {"currency": {"code": "EUR"}}},
                    {"operationAmount": {"currency": {"code": "USD"}}},
                    {"operationAmount": {"currency": {"code": "GBP"}}},
                ],
                "USD",
                [{"operationAmount": {"currency": {"code": "USD"}}}],
        ),
        # Тест с несколькими транзакциями, все из которых совпадают по валюте
        (
                [{"operationAmount": {"currency": {"code": "USD"}}},
                 {"operationAmount": {"currency": {"code": "USD"}}}],
                "USD",
                [{"operationAmount": {"currency": {"code": "USD"}}},
                 {"operationAmount": {"currency": {"code": "USD"}}}],
        ),
    ],
)
def test_filter_by_currency(transactions: Iterable[dict], currency_code: str, expected: Iterable[dict]) -> None:
    assert list(filter_by_currency(transactions, currency_code)) == expected


def test_transaction_descriptions(sample_transactions):
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == [
        'Перевод средств',
        'Оплата услуг',
        'Покупка товаров',
        'Перевод на карту'
    ]


def test_card_number_generator():
    generated_numbers = list(card_number_generator(1, 5))
    assert generated_numbers == [
        '0000 0000 0000 0001',
        '0000 0000 0000 0002',
        '0000 0000 0000 0003',
        '0000 0000 0000 0004',
        '0000 0000 0000 0005'
    ]
