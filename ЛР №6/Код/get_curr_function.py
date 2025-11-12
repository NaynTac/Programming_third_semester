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