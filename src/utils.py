import json
import logging
import os
from src.external_api import transactions_total
import re
from collections import Counter

# Настройка логгера для модуля utils
LOG_DIR = "logs"
LOG_FILE_UTILS = os.path.join(LOG_DIR, "utils.log")

# Создаем папку logs, если она не существует
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Создаем логгер для модуля utils
utils_logger = logging.getLogger("utils_logger")
utils_logger.setLevel(logging.INFO)  # Уровень логирования

# Создаем обработчик для записи логов в файл для модуля utils
utils_file_handler = logging.FileHandler(LOG_FILE_UTILS, mode='w', encoding='utf-8')

# Создаем форматтер для логов для модуля utils
utils_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
utils_file_handler.setFormatter(utils_formatter)

# Добавляем обработчик к логгеру для модуля utils
utils_logger.addHandler(utils_file_handler)


def load_transactions(file_path: str) -> list[dict]:
    """
    Загружает данные о финансовых транзакциях из JSON-файла.
    Возвращает список словарей с данными о транзакциях.
    Если файл пустой, содержит не список или не найден, возвращает пустой список.
    """
    utils_logger.info(f"Загрузка транзакций из файла: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                utils_logger.info(f"Успешно загружено {len(data)} транзакций из файла: {file_path}")
                return data
            else:
                utils_logger.warning(
                    f"Файл {file_path} содержит данные не в формате списка. Возвращается пустой список.")
                return []
    except FileNotFoundError:
        utils_logger.error(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError:
        utils_logger.error(f"Ошибка декодирования JSON в файле: {file_path}")
        return []
    except Exception as exception:
        utils_logger.exception(
            f"Произошла ошибка при чтении файла: {exception}")  # Используем logger.exception для трассировки
        return []


if __name__ == '__main__':
    # Пример использования (после реализации utils.py и наличия operations.json)
    transactions = load_transactions("../data/operations.json")
    if transactions:
        for transaction in transactions:
            try:
                total_rub = transactions_total(transaction)
                utils_logger.info(f"Сумма транзакции в рублях: {total_rub}")
                print(f"Сумма транзакции в рублях: {total_rub}")
            except KeyError as e:
                utils_logger.error(f"Отсутствует ключ {e} в транзакции: {transaction}")
                print(f"Ошибка: Отсутствует ключ {e} в транзакции: {transaction}")
            except Exception as e:
                utils_logger.exception(f"Произошла ошибка при обработке транзакции: {e}")
                print(f"Произошла ошибка при обработке транзакции: {e}")

    else:
        utils_logger.warning("Нет данных о транзакциях для обработки.")
        print("Нет данных о транзакциях для обработки.")


def find_transactions_by_description(transactions, search_string):
    """
    Фильтрует список транзакций, возвращая те, в описании которых содержится заданная строка поиска.

    Args:
        transactions (list): Список словарей с данными о банковских операциях.
        search_string (str): Строка для поиска в описании транзакций.

    Returns:
        list: Список словарей с операциями, у которых в описании есть строка поиска.
    """
    return [
        transaction
        for transaction in transactions
        if re.search(search_string, transaction.get("description", ""), re.IGNORECASE)
    ]


def count_transaction_categories(transactions):
    """
    Подсчитывает количество банковских операций каждого типа (категории).

    Args:
        transactions (list): Список словарей с данными о банковских операциях.

    Returns:
        dict: Словарь, где ключи - названия категорий, а значения - количество операций в каждой категории.
    """
    categories = [transaction.get("description", "") for transaction in transactions]
    return Counter(categories)
