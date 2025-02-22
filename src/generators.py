def filter_by_currency(transactions, currency='USD'):
    """
    Генератор, который возвращает транзакции с заданной валютой.
    :param transactions: Список словарей с транзакциями.
    :param currency: Строка с требуемой валютой (по умолчанию 'USD').
    :yield: Транзакция, соответствующая указанной валюте.
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions):
    """
    Генератор, который поочередно возвращает описание каждой транзакции.
    :param transactions: Список словарей с транзакциями.
    :yield: Описание транзакции.
    """
    for transaction in transactions:
        yield transaction.get('description', 'Без описания')


def card_number_generator(start=1, end=9999999999999999):
    """
    Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX.
    :param start: Начальное значение диапазона.
    :param end: Конечное значение диапазона.
    :yield: Сгенерированный номер карты в формате XXXX XXXX XXXX XXXX.
    """
    for number in range(start, end + 1):
        yield (f"{str(number).zfill(16)[:4]}"
               f" {str(number).zfill(16)[4:8]} {str(number).zfill(16)[8:12]} {str(number).zfill(16)[12:]}")
