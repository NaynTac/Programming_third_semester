from models import Author
from models import App
from models import User
from models import Currency
from models import UserCurrency

from utils.currencies_api import get_currencies

import http.server
import urllib.parse
from jinja2 import Environment, PackageLoader, select_autoescape


env = Environment( loader=PackageLoader("myapp"), autoescape=select_autoescape())

template_index = env.get_template("index.html")
template_users = env.get_template("users.html")
template_currencies = env.get_template("currencies.html")
template_author = env.get_template("author.html")
template_user_id = env.get_template("user_id.html")


main_author = Author(name="Пименов Егор", group="2об_ИВТ-2/24")
main_app = App("myapp", "1.0.0", main_author)

users_list = list()
currencies_list = list()
uc_list = list()

for i in range(1, 4):
	user = User(id=i, name=f"User №{i}")
	users_list.append(user)

currency_list = ["AUD", "AZN", "DZD", "GBP", "EUR", "USD", "AMD", "BHD", "BRL"]
data = get_currencies(currency_list)

for code, values in data.items():
	c = Currency(id=values["ID"], num_code=None, char_code=code, name=None, value=values["Value"], nominal=None)
	currencies_list.append(c)

for i in range(len(currencies_list)):
	uc = UserCurrency(id=i + 1, user_id=users_list[i % 3].id, currency_id=currencies_list[i].id)
	uc_list.append(uc)


index_content = template_index.render(
	navigation=[{"caption": "", "href": "/"}]
	)

users_content = template_users.render(
	users=users_list,
	navigation=[{"caption": "", "href": "/users"}]
	)

currencies_content = template_currencies.render(
	currencies=currencies_list,
	navigation=[{"caption": "", "href": "/currencies"}]
	)

author_content = template_author.render(
	author_name=main_author.name,
	author_group=main_author.group,
	navigation=[{"caption": "", "href": "/author"}]
	)

templates = {
	"/": index_content,
	"/users": users_content,
	"/currencies": currencies_content,
	"/author": author_content,
	}


class CustomHandler(http.server.BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
		if "?id=" in self.path:
			parsed_data = urllib.parse.parse_qs(self.path, separator="?")
			user_id = int(parsed_data["id"][0])
			uc_ids = [user.currency_id for user in uc_list if user.user_id == user_id]
			uc_currencies = [c for c in currencies_list if c.id in uc_ids]

			user_id_content = template_user_id.render(
				id=user_id,
				currencies=uc_currencies,
				navigation=[{"caption": "", "href": f"/user?id={parsed_data["id"]}"}]
			)

			self.wfile.write(bytes(user_id_content.encode("utf-8")))
		else:
			self.wfile.write(bytes(templates[self.path].encode("utf-8")))


PORT = 8000
with http.server.HTTPServer(("", PORT), CustomHandler) as httpd:
	print(f"Сервер запущен!")

	httpd.serve_forever()