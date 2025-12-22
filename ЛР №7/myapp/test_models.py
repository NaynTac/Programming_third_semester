from models import *
import pytest


"""Тестирование геттеров"""
@pytest.mark.parametrize("name, version, author",
	[("test_name", "test_version", Author("test_name", "test_group"))])
def test_app_getter(name, version, author):

	test_app = App(name=name, version=version, author=author)

	assert test_app.name == name
	assert test_app.version == version
	assert test_app.author == author


@pytest.mark.parametrize("name, group", [("test_name", "test_group")])
def test_author_getter(name, group):

	test_author = Author(name=name, group=group)

	assert test_author.name == name
	assert test_author.group == group


@pytest.mark.parametrize("id, num_code, char_code, name, value, nominal",
	[("test_id", "test_num_code", "test_char_code", "test_name", 0.12345, 100)])
def test_currency_getter(id, num_code, char_code, name, value, nominal):

	test_currency = Currency(id=id, num_code=num_code, char_code=char_code, name=name,
		value=value, nominal=nominal)

	assert test_currency.id == id
	assert test_currency.num_code == num_code
	assert test_currency.char_code == char_code
	assert test_currency.name == name
	assert test_currency.value == value
	assert test_currency.nominal == nominal


@pytest.mark.parametrize("id, name", [("test_id", "test_name")])
def test_user_getter(id, name):

	test_user = User(id=id, name=name)

	assert test_user.id == id
	assert test_user.name == name


@pytest.mark.parametrize("id, user_id, currency_id",
	[("test_id", "test_user_id", "test_currency_id")])
def test_user_currency_getter(id, user_id, currency_id):

	test_user_currency = UserCurrency(id=id, user_id=user_id, currency_id=currency_id)

	assert test_user_currency.id == id
	assert test_user_currency.user_id == user_id
	assert test_user_currency.currency_id == currency_id


"""Тестирование сеттеров"""
@pytest.mark.parametrize("name, version, author",
	[("test_name", "test_version", Author("test_name", "test_group"))])
def test_app_setter(name, version, author):

	test_app = App(name=None, version=None, author=None)

	test_app.name = name
	test_app.version = version
	test_app.author = author

	assert test_app.name == name
	assert test_app.version == version
	assert test_app.author == author


@pytest.mark.parametrize("name, group", [("test_name", "test_group")])
def test_author_setter(name, group):

	test_author = Author(name=None, group=None)

	test_author.name = name
	test_author.group = group

	assert test_author.name == name
	assert test_author.group == group


@pytest.mark.parametrize("num_code, char_code, name, value, nominal",
	[("tnc", "tcc", "test_name", 0.12345, 100)])
def test_currency_setter(num_code, char_code, name, value, nominal):

	test_currency = Currency(id=None, num_code=None, char_code=None, name=None,
		value=None, nominal=None)

	test_currency.num_code = num_code
	test_currency.char_code = char_code
	test_currency.name = name
	test_currency.value = value
	test_currency.nominal = nominal

	assert test_currency.num_code == num_code
	assert test_currency.char_code == char_code
	assert test_currency.name == name
	assert test_currency.value == value
	assert test_currency.nominal == nominal


@pytest.mark.parametrize("name", [("test_name")])
def test_user_setter(name):

	test_user = User(id=None, name=None)

	test_user.name = name

	assert test_user.name == name


"""Тестирование исключений"""
@pytest.mark.parametrize("name, version, author", [
	("tn", "test_version", Author("test_name", "test_group")),
	("test_name", "tv", Author("test_name", "test_group")),
	("test_name", "test_version", 115)
	])
def test_app_exep(name, version, author):
	with pytest.raises(ValueError):
		test_app = App(name=None, version=None, author=None)	

		test_app.name = name
		test_app.version = version
		test_app.author = author


@pytest.mark.parametrize("name, group", [
	("tn", "test_group"),
	("test_name", "tg")
	])
def test_author_exep(name, group):
	with pytest.raises(ValueError):
		test_author = Author(name=None, group=None)

		test_author.name = name
		test_author.group = group


@pytest.mark.parametrize("num_code, char_code, name, value, nominal", [
	("test", "tcc", "test_name", 0.12345, 100),
	("tnc", "test", "test_name", 0.12345, 100),
	("tnc", "tcc", None, 0.12345, 100),
	("tnc", "tcc", "test_name", "test", 100),
	("tnc", "tcc", "test_name", 0.12345, 0.12345)
	])
def test_currency_exep(num_code, char_code, name, value, nominal):
	with pytest.raises(ValueError):
		test_currency = Currency(id=None, num_code=None, char_code=None, name=None,
			value=None, nominal=None)

		test_currency.num_code = num_code
		test_currency.char_code = char_code
		test_currency.name = name
		test_currency.value = value
		test_currency.nominal = nominal


@pytest.mark.parametrize("name", [("tn")])
def test_user_exep(name):
	with pytest.raises(ValueError):
		test_user = User(id=None, name=None)

		test_user.name = name