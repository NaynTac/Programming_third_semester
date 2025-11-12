# Лабораторная работа №4
**Задача**: Написать функцию get_currencies(currency_codes, url), которая обращается к API по url (по умолчанию - https://www.cbr-xml-daily.ru/daily_json.js) и возвращает словарь курсов валют для валют из списка currency_codes. В возвращаемом словаре ключи - символьные коды валют, а значения - их курсы. В случае ошибки запроса функция должна вернуть None.
___

**Код**:
```python
import requests
import logging
import sys

# Определяем логгер
logging.getLogger("mainLogger")
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

# Создаем декоратор, который будет формировать лог
def log(func):

    def get_curr(*args):

        logger.info("Getting request")

        try:
            result = func(*args)
            logger.info("Successfully")
            return result
        # Обработка исключений
        except requests.exceptions.HTTPError as ex: logger.error(f"{str(ex)}")
        except requests.exceptions.InvalidSchema as ex: logger.error(f"{str(ex)}")
        except requests.exceptions.ConnectionError: logger.error(f"Connection Error")
        except requests.exceptions.InvalidURL: logger.error(f"Invalid URL")
        except KeyError as ex: logger.error(f"Currency key not defined ({str(ex)})")

    return get_curr


@log
def get_currencies(currency_codes, url):
    # Обращение по url
    req = requests.get(url)
    # Если обращение было неудачным, то бросаем исключение
    if req.status_code != 200: req.raise_for_status()
    # Забираем данные
    data = req.json()["Valute"]
    result = dict()
    # Добавляем нужные данные в итоговый словарь
    for code in currency_codes:
        result[code] = data[code]["Value"]

    return result


if __name__ == "__main__":
    get_currencies(["USD"], "https://www.cbr-xml-daily.ru/daily_json.js")
```
___
**Тесты функции**:
```python
from get_curr_function import get_currencies
import requests

url = "https://www.cbr-xml-daily.ru/daily_json.js"
req = requests.get(url)
data = req.json()["Valute"]


if __name__ == "__main__":
    
    import unittest
    
    class TestFunction(unittest.TestCase):
        
        def test_1(self):
            self.assertEqual(get_currencies(["USD"], url), {"USD": data["USD"]["Value"]})
            
        def test_2(self):
            self.assertEqual(get_currencies(["AUD"], url), {"AUD": data["AUD"]["Value"]})
            
        def test_3(self):
            self.assertEqual(get_currencies(["AZN", "DZD"], url),
                {"AZN": data["AZN"]["Value"], "DZD": data["DZD"]["Value"]})

        def test_4(self):
            self.assertEqual(get_currencies(["AZN", "RUT"], url), None)

    unittest.main()
```
**Результат тестов**:
```
INFO:get_curr_function:Getting request
INFO:get_curr_function:Successfully
.INFO:get_curr_function:Getting request
INFO:get_curr_function:Successfully
.INFO:get_curr_function:Getting request
INFO:get_curr_function:Successfully
.INFO:get_curr_function:Getting request
ERROR:get_curr_function:Currency key not defined ('RUT')
.
----------------------------------------------------------------------
Ran 4 tests in 1.352s

OK
[Finished in 2.0s]
```
