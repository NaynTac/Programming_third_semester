from utils.currencies_api import get_currencies
import pytest
import requests


@pytest.mark.parametrize("codes", [(["USD"]), (["BRL", "USD", "VND", "EUR"])])
def test_currency_eur(codes):

	currency_data = get_currencies(codes)

	for code in currency_data.keys():
		assert code in currency_data
		assert isinstance(currency_data[code]["Value"], float)
		assert currency_data[code]["Value"] > 0


def test_nonexist_code():
	assert "не найден" in get_currencies(["ABC"])["ABC"]


def test_error():
	with pytest.raises(requests.exceptions.RequestException):
		currency_data = get_currencies(None, url="https://jjfjj.js")