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
				currencies[code] = {"Value": data["Valute"][code]["Value"], "ID": data["Valute"][code]["ID"]}
			else:
				currencies[code] = f"Код валюты '{code}' не найден."

	return currencies