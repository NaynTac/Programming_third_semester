class App():

	def __init__(self, name, version, author):
		self.__name = name
		self.__version = version
		self.__author = author

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, name):
		if isinstance(name, str) and len(name) > 2:
			self.__name = name
		else:
			raise ValueError("Ошибка при задании навзания приложения")

	@property
	def version(self):
		return self.__version
	
	@version.setter
	def version(self, version):
		if isinstance(version, str) and len(version) > 3:
			self.__version = version
		else:
			raise ValueError("Ошибка при задании версии приложения")

	@property
	def author(self):
		return self.__author

	@author.setter
	def author(self, author):
		if isinstance(author, Author):
			self.__author = author
		else:
			raise ValueError("Ошибка при задании автора приложения")
	
	