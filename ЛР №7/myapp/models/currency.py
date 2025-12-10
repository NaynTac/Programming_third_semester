class Currency():
	
	def __init__(self, id, num_code, char_code, name, value, nominal):
		self.__id = id
		self.__num_code = num_code
		self.__char_code = char_code
		self.__name = name
		self.__value = value
		self.__nominal = nominal

	@property
	def id(self):
		return self.__id
	
	@property
	def num_code(self):	
		return self.__num_code
	
	@num_code.setter
	def num_code(self, num_code):
		if isinstance(str, num_code) and len(num_code) == 3:
			self.__num_code = num_code
		else:
			raise ValueError("Ошибка при задании цифрового кода валюты")

	@property
	def char_code(self):
		return self.__char_code
	
	@char_code.setter
	def char_code(self, char_code):
		if isinstance(str, char_code) and len(char_code) == 3:
			self.__char_code = char_code
		else:
			raise ValueError("Ошибка при задании символьного кода валюты")

	@property
	def name(self):
		return self.__name
	
	@name.setter
	def name(self, name):
		if isinstance(str, name) and name:
			self.__name = name
		else:
			raise ValueError("Ошибка при задании названия валюты")

	@property
	def value(self):
		return self.__value
	
	@value.setter
	def value(self, value):
		if isinstance(float, value) and value > 0:
			self.__value = value
		else:
			raise ValueError("Ошибка при задании курса валюты")

	@property
	def nominal(self):
		return self.__nominal
	
	@nominal.setter
	def nominal(self, nominal):
		if isinstance(int, nominal) and nominal > 0:
			self.__nominal = nominal
		else:
			raise ValueError("Ошибка при задании номинала валюты")