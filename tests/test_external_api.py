import unittest
from unittest.mock import patch, MagicMock
from src.external_api import transactions_total
from src.external_api import convert_to_rub


class TestExternalAPI(unittest.TestCase):

    @patch('requests.get')  # Или src.external_api, если вынесли функцию туда
    def test_convert_to_rub_success(self, mock_get):
        # Arrange
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 75.50}  # Пример ответа API
        mock_get.return_value = mock_response

        # Act
        result = convert_to_rub(1.0, "USD")

        # Assert
        self.assertEqual(result, 75.50)
        mock_get.assert_called_once()

    @patch('requests.get')  # Или src.external_api, если вынесли функцию туда
    def test_convert_to_rub_failure(self, mock_get):
        # Arrange
        mock_response = MagicMock()
        mock_response.status_code = 500  # Имитация ошибки API
        mock_response.text = "Internal Server Error"
        mock_get.return_value = mock_response

        # Act
        result = convert_to_rub(1.0, "EUR")

        # Assert
        self.assertEqual(result, 0.0)  # Или self.assertRaises, если вы поднимаете исключение в случае ошибки

    def test_transactions_total_rub(self):
        transaction = {
            "operationAmount": {
                "amount": "100.00",
                "currency": {
                    "code": "RUB"
                }
            }
        }
        result = transactions_total(transaction)
        self.assertEqual(result, 100.00)

    @patch('src.external_api.convert_to_rub')  # Или src.external_api, если вынесли функцию туда
    def test_transactions_total_usd(self, mock_convert_to_rub):
        # Arrange
        transaction = {
            "operationAmount": {
                "amount": "1.0",
                "currency": {
                    "code": "USD"
                }
            }
        }
        mock_convert_to_rub.return_value = 75.0  # Mock курс

        # Act
        result = transactions_total(transaction)

        # Assert
        self.assertEqual(result, 75.0)
        mock_convert_to_rub.assert_called_once_with(1.0, "USD")
