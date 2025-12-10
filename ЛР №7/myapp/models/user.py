class User():

	def __init__(self, id, name):
		self.__id = id
		self.__name = name

	@property
	def id(self):
		return self.__id

	@property
	def name(self):
		return self.__name
	
	@name.setter
	def name(self, name):
		if isinstance(str, name) and len(name) > 2:
			self.__name = name
		else:
			raise ValueError("Ошибка при задании имени пользователя")
