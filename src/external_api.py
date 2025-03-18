import os
from dotenv import load_dotenv
from pathlib import Path
import requests

load_dotenv()
current_dir = Path(__file__).parent.parent.resolve()
operations_file_json = current_dir / 'data' / 'operations.json'
API_KEY = os.getenv('API_KEY')


def transactions_total(transaction: dict) -> float:
    """
    Принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API
    для получения текущего курса валют и конвертации суммы операции в рубли.
    """
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount
    else:
        return convert_to_rub(amount, currency)


def convert_to_rub(amount: float, currency: str) -> float:
    """
    Конвертирует сумму из указанной валюты в рубли, используя API.
    """
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    headers = {"apikey": API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return float(data["result"])
    else:
        print(f"Ошибка при запросе к API: {response.status_code} - {response.text}")
        return 0.0  # Или можно поднять исключение, если не удалось сконвертировать
