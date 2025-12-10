class UserCurrency():
	
	def __init__(self, id, user_id, currency_id):
		self.__id = id
		self.__user_id = user_id
		self.__currency_id = currency_id

	@property
	def id(self):
		return self.__id

	@property
	def user_id(self):
		return self.__user_id

	@property
	def currency_id(self):
		return self.__currency_id
	