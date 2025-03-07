import json
from src.external_api import transactions_total


def load_transactions(file_path: str) -> list[dict]:
    """
    Загружает данные о финансовых транзакциях из JSON-файла.
    Возвращает список словарей с данными о транзакциях.
    Если файл пустой, содержит не список или не найден, возвращает пустой список.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")  # Добавляем логирование
        return []
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON в файле: {file_path}")  # Добавляем логирование
        return []
    except Exception as exception:
        print(f"Произошла ошибка при чтении файла: {exception}")
        return []


if __name__ == '__main__':
    # Пример использования (после реализации utils.py и наличия operations.json)
    transactions = load_transactions("../data/operations.json")
    if transactions:
        for transaction in transactions:
            try:
                total_rub = transactions_total(transaction)
                print(f"Сумма транзакции в рублях: {total_rub}")
            except KeyError as e:
                print(f"Ошибка: Отсутствует ключ {e} в транзакции: {transaction}")
            except Exception as e:
                print(f"Произошла ошибка при обработке транзакции: {e}")

    else:
        print("Нет данных о транзакциях для обработки.")
