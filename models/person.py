class Person:

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	def __str__(self):
		return "First Name: {0} Last Name: {1}".format(self.first_name, self.last_name)


	