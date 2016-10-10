from  models.person import Person

class Staff(Person):

	staff_cache = []
	def __init__(self, first_name, last_name):
		super(Staff, self).__init__(first_name, last_name)
		full_name = self.first_name + " " + self.last_name
		Staff.staff_cache.append(full_name)

