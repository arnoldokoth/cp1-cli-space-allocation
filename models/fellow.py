from models.person import Person


class Fellow(Person):
	fellow_cache = []

	def __init__(self, first_name, last_name):
		Person.__init__(self, first_name, last_name)
		full_name = self.first_name + " " + self.last_name
		Fellow.fellow_cache.append(full_name)

	@staticmethod
	def get_fellow_cache():
		return Fellow.fellow_cache

