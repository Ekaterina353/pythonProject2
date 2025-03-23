import pandas as pd
from unittest.mock import patch, MagicMock
from src.transactions_reader import read_transaction_csv, read_transaction_excel


@patch("pandas.read_csv")
def test_read_transaction_csv_success(mock_readr_csv):
    # Мокируем pd.read_csv чтобы вернуть DataFrame
    mock_readr_csv.return_value = pd.DataFrame({'date': ['2023-11-15'], 'amount': [100], 'description': ['Test']})
    #with patch('transactions_reader.pd.read_csv', return_value=mock_df):
    #    result = read_transaction_csv('dummy.csv')
    result = read_transaction_csv("test_csv")
    assert result == [{'date': '2023-11-15', 'amount': 100, 'description': 'Test'}]

def test_read_transaction_csv_file_not_found():
    # Проверяем, что возвращается пустой список и выводится сообщение об ошибке
    result = read_transaction_csv('nonexistent.csv')
    assert result == []


def test_read_transaction_excel_success():
    # Мокируем pd.read_excel
    mock_df = pd.DataFrame([{'date': '2023-11-16', 'amount': 200, 'description': 'Test Excel'}])
    with patch('src.transactions_reader.pd.read_excel', return_value=mock_df):
        result = read_transaction_excel('dummy.xlsx')
        assert result == [{'date': '2023-11-16', 'amount': 200, 'description': 'Test Excel'}]


def test_read_transaction_excel_file_not_found():
    # Проверяем обработку несуществующего файла Excel
    result = read_transaction_excel('nonexistent.xlsx')
    assert result == []
