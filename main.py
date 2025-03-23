import json
import csv
import openpyxl
from src.utils import find_transactions_by_description
from src.masks import get_mask_card_number, get_mask_account


def read_json_file(file_path):
    """Считывает данные из JSON файла."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def read_csv_file(file_path):
    """Считывает данные из CSV файла."""
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)


def read_excel_file(file_path):
    """Считывает данные из Excel файла."""
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    header = [cell.value for cell in sheet[1]]
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append(dict(zip(header, row)))
    return data


def format_transaction(transaction):
    """Форматирует транзакцию для вывода."""
    date = transaction.get("date", "N/A")[:10]  # Обрезаем время
    description = transaction.get("description", "N/A")
    from_account = transaction.get("from", "")
    to_account = transaction.get("to", "")
    amount = transaction.get("operationAmount", {}).get("amount", "N/A")
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("name", "N/A")

    if from_account:
        from_account = get_mask_card_number(from_account) if "card" in from_account.lower() else get_mask_account(
            from_account)
    if to_account:
        to_account = get_mask_card_number(to_account) if "card" in to_account.lower() else get_mask_account(to_account)

    if from_account and to_account:
        info = f"{from_account} -> {to_account}"
    elif from_account:
        info = from_account
    elif to_account:
        info = to_account
    else:
        info = "N/A"

    return f"{date} {description}\n{info}\nСумма: {amount} {currency}\n"


def main():
    """Основная функция программы."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:
        print("\nВыберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        choice = input()

        if choice == '1':
            file_path = "data/operations.json"
            transactions = read_json_file(file_path)
            print("Для обработки выбран JSON-файл.")
            break
        elif choice == '2':
            file_path = "data/transactions.csv"
            transactions = read_csv_file(file_path)
            print("Для обработки выбран CSV-файл.")
            break
        elif choice == '3':
            file_path = "data/transactions_exsel.xlsx"
            transactions = read_excel_file(file_path)
            print("Для обработки выбран XLSX-файл.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите пункт меню 1, 2 или 3.")

    # Фильтрация по статусу
    available_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status = input(
            f"Введите статус, по которому необходимо выполнить фильтрацию. "
            f"Доступные для фильтровки статусы: {', '.join(available_statuses)}\n").upper()
        if status in available_statuses:
            print(f"Операции отфильтрованы по статусу \"{status}\"")
            transactions = [t for t in transactions if t.get("state", "").upper() == status]
            break
        else:
            print(f"Статус операции \"{status}\" недоступен.")

    # Сортировка по дате
    sort_by_date = input("Отсортировать операции по дате? Да/Нет\n").lower()
    if sort_by_date == "да":
        order = input("Отсортировать по возрастанию или по убыванию?\n").lower()
        reverse = order == "по убыванию"
        transactions.sort(key=lambda x: x.get("date", ""), reverse=reverse)

    # Фильтрация по рублю
    ruble_only = input("Выводить только рублевые тразакции? Да/Нет\n").lower()
    if ruble_only == "да":
        transactions = [t for t in transactions if
                        t.get("operationAmount", {}).get("currency", {}).get("name") == "RUB"]

    # Фильтрация по слову в описании
    filter_by_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower()
    if filter_by_word == "да":
        search_word = input("Введите слово для поиска:\n")
        transactions = find_transactions_by_description(transactions, search_word)

    print("Распечатываю итоговый список транзакций…")
    if transactions:
        print(f"Всего банковских операций в выборке: {len(transactions)}")
        for transaction in transactions:
            print(format_transaction(transaction))
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()
