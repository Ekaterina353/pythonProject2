import unittest
from src.masks import get_mask_card_number, get_mask_account


class TestMaskingFunctions(unittest.TestCase):
    def test_get_mask_card_number_valid(self):
        self.assertEqual(get_mask_card_number("1234567890123456"), "1234 56** **** 3456")
        self.assertEqual(get_mask_card_number("0000000000000000"), "0000 00** **** 0000")
        self.assertEqual(get_mask_card_number("9999999999999999"), "9999 99** **** 9999")

    def test_get_mask_card_number_invalid_length(self):
        with self.assertRaises(ValueError) as context:
            get_mask_card_number("123456789012345")  # Length 15
        self.assertEqual(str(context.exception), "Номер карты должен состоять из 16 цифр")

        with self.assertRaises(ValueError) as context:
            get_mask_card_number("12345678901234567")  # Length 17
        self.assertEqual(str(context.exception), "Номер карты должен состоять из 16 цифр")

    def test_get_mask_card_number_invalid_characters(self):
        with self.assertRaises(ValueError) as context:
            get_mask_card_number("123456789012345a")
        self.assertEqual(str(context.exception), "Номер карты должен состоять из 16 цифр")

        with self.assertRaises(ValueError) as context:
            get_mask_card_number("1234 5678 9012 3456")
        self.assertEqual(str(context.exception), "Номер карты должен состоять из 16 цифр")

    def test_get_mask_card_number_empty_string(self):
        with self.assertRaises(ValueError) as context:
            get_mask_card_number("")
        self.assertEqual(str(context.exception), "Номер карты должен состоять из 16 цифр")

    def test_get_mask_account_valid(self):
        self.assertEqual(get_mask_account("1234567890"), "**7890")
        self.assertEqual(get_mask_account("0000"), "**0000")
        self.assertEqual(get_mask_account("99999999"), "**9999")
        self.assertEqual(get_mask_account("1234"), "**1234")

    def test_get_mask_account_invalid_length(self):
        with self.assertRaises(ValueError) as context:
            get_mask_account("123")
        self.assertEqual(str(context.exception), "Номер счета должен состоять минимум из 4 цифр")

    def test_get_mask_account_invalid_characters(self):
        with self.assertRaises(ValueError) as context:
            get_mask_account("123a")
        self.assertEqual(str(context.exception), "Номер счета должен состоять минимум из 4 цифр")
        with self.assertRaises(ValueError) as context:
            get_mask_account("abcde")
        self.assertEqual(str(context.exception), "Номер счета должен состоять минимум из 4 цифр")

    def test_get_mask_account_empty_string(self):
        with self.assertRaises(ValueError) as context:
            get_mask_account("")
        self.assertEqual(str(context.exception), "Номер счета должен состоять минимум из 4 цифр")
