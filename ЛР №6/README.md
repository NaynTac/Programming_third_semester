# Лабораторная работа №6
**Задача**: Написать функцию get_currencies(currency_codes, url), которая обращается к API по url (по умолчанию - https://www.cbr-xml-daily.ru/daily_json.js) и возвращает словарь курсов валют для валют из списка currency_codes. В возвращаемом словаре ключи - символьные коды валют, а значения - их курсы. В случае ошибки запроса функция должна вернуть None.
___

**Код**:
```python
from functools import wraps
import requests
import logging
import sys


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def trace(func=None, handle=sys.stdout):
    if not func:
        return lambda func: trace(func, handle=handle)
    else:
        print(f"{func.__name__}, {handle}")

    @wraps(func)
    def inner(*args, **kwargs):

        try:
            return func(*args, **kwargs)

        except requests.exceptions.RequestException as exc:

            if handle == sys.stdout:
                handle.write(f"Ошибка при запросе к API: {exc}")
            elif handle == logging.getLogger(__name__):
                handle.error(f"Ошибка при запросе к API: {exc}")

            raise requests.exceptions.RequestException("Упали с исключением")

    return inner


@trace
def get_currencies(currency_codes:list, url:str="https://www.cbr-xml-daily.ru/daily_json.js") -> dict:
    """
    Получает курс валют API Центробанка России

    Args:
        currency_codes (list): Список символьных кодов валют (Например, ["USD", "EUR"])

    Returns:
        dict: Словарь вида {символьный код валюты: курс валюты, }
            В случае ошибки запроса возвращает None
    """
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    currencies = dict()

    if "Valute" in data:
        for code in currency_codes:
            if code in data["Valute"]:
                currencies[code] = data["Valute"][code]["Value"]
            else:
                currencies[code] = f"Код валюты '{code}' не найден."

    return currencies
```
___
**Тесты функции**:
```python
from get_currencies import get_currencies
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
```
**Результат тестов**:
```
get_currencies, <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>
test_currency_eur (__main__.TestFunction.test_currency_eur)
Проверяет наличие ключа в словаре и значения этого ключа ... ok
test_error (__main__.TestFunction.test_error) ... Ошибка при запросе к API: HTTPSConnectionPool(host='jjfjj.js', port=443): Max retries exceeded with url: / (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x000001C729651590>: Failed to resolve 'jjfjj.js' ([Errno 11001] getaddrinfo failed)"))ok
test_nonexist_code (__main__.TestFunction.test_nonexist_code) ... ok

----------------------------------------------------------------------
Ran 3 tests in 1.073s

OK
```
