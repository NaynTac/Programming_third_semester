from get_currencies import get_currencies
from unittest.mock import patch
from io import StringIO
import requests


if __name__ == "__main__":
    
    import unittest
    
    class TestFunction(unittest.TestCase):
        
        def test_currency_eur(self):
            """
            Проверяет наличие ключа в словаре и значения этого ключа
            """
            currency_data = get_currencies(["EUR"])

            self.assertIn("EUR", currency_data)
            self.assertIsInstance(currency_data["EUR"], float)
            self.assertGreaterEqual(currency_data["EUR"], 0)

        def test_nonexist_code(self):
            self.assertIn("не найден", get_currencies(["AAA"])["AAA"])

        def test_error(self):
            error_phrase = "Ошибка при запросе к API"
            currency_list = ["EUR"]

            with self.assertRaises(requests.exceptions.RequestException):
                currency_data = get_currencies(currency_list, url="https://jjfjj.js")


    unittest.main(argv=[''], verbosity=2, exit=False)