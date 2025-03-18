import unittest
from unittest.mock import mock_open, patch
from src.utils import load_transactions
from pathlib import Path
import json


class TestUtils(unittest.TestCase):

    def test_load_transactions_success(self):
        # Arrange
        data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
        json_data = json.dumps(data)
        file_path = "test_file.json"  # Используем строковый путь
        with patch("builtins.open", mock_open(read_data=json_data)) as mock_file:
            # Устанавливаем возвращаемое значение для Path.exists() равным True
            with patch("pathlib.Path.exists", return_value=True):
                # Act
                transactions = load_transactions(file_path)
                # Assert
                self.assertEqual(transactions, data)
                mock_file.assert_called_with(file_path, 'r', encoding='utf-8')

    def test_load_transactions_empty_file(self):
        with patch("builtins.open", mock_open(read_data="")):
            with patch("pathlib.Path.exists", return_value=True):
                transactions = load_transactions("empty.json")
                self.assertEqual(transactions, [])

    def test_load_transactions_invalid_json(self):
        with patch("builtins.open", mock_open(read_data="invalid json")):
            with patch("pathlib.Path.exists", return_value=True):
                transactions = load_transactions("invalid.json")
                self.assertEqual(transactions, [])

    def test_load_transactions_file_not_found(self):
        with patch("builtins.open", side_effect=FileNotFoundError):
            transactions = load_transactions("nonexistent.json")
            self.assertEqual(transactions, [])

    def test_load_transactions_not_a_list(self):
        with patch("builtins.open", mock_open(read_data=json.dumps({"key": "value"}))):
            with patch("pathlib.Path.exists", return_value=True):
                transactions = load_transactions("not_a_list.json")
                self.assertEqual(transactions, [])


if __name__ == '__main__':
    unittest.main()
