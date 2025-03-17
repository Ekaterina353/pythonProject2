import pandas as pd
import os


def read_transaction_csv(file_csv: str) -> list:
    """Функция считывает финансовые операции из CSV-файла.
    Args:
        file_csv (str): Путь к CSV-файлу.
    Returns:
        list: Список словарей, где каждый словарь представляет собой транзакцию.
    """
    try:
        reader = pd.read_csv(file_csv, sep=";")
        return reader.to_dict(orient="records")
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_csv} не найден.")
        return []
    except Exception as e:
        print(f"Ошибка при чтении CSV-файла: {e}")
        return []


def read_transaction_excel(file_excel: str) -> list:
    """Функция считывает финансовые операции из XLSX-файла.
    Args:
        file_excel (str): Путь к XLSX-файлу.
    Returns:
        list: Список словарей, где каждый словарь представляет собой транзакцию.
    """
    try:
        reader = pd.read_excel(file_excel)
        return reader.to_dict(orient="records")
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_excel} не найден.")
        return []

    except Exception as e:
        print(f"Ошибка при чтении Excel-файла: {e}")
        return []


if __name__ == '__main__':

    # Пример использования (создайте тестовые файлы)

    csv_file = "transactions.csv"
    excel_file = "transactions.xlsx"

    # Создаем пример CSV-файла

    if not os.path.exists(csv_file):
        with open(csv_file, "w") as f:
            f.write("date;amount;description\n")
            f.write("2023-10-26;100;Покупка\n")
            f.write("2023-10-27;-50;Возврат\n")

    # Создаем пример Excel-файла

    if not os.path.exists(excel_file):
        df = pd.DataFrame({
            "date": ["2023-10-28", "2023-10-29"],
            "amount": [200, -75],
            "description": ["Зарплата", "Оплата счетов"]
        })
        df.to_excel(excel_file, index=False)
    csv_transactions = read_transaction_csv(csv_file)
    excel_transactions = read_transaction_excel(excel_file)
    print("Транзакции из CSV:", csv_transactions)
    print("Транзакции из Excel:", excel_transactions)
