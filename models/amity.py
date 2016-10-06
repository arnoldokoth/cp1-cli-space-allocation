import random

from person import Person
from staff import Staff
from fellow import Fellow


class Amity:

	# Application Data 
	offices = []
	living_spaces = []
	fellows = []
	staff = []
	room_allocations = {}

	@staticmethod
	def create_room(room_type, *args):
		pass
		# for room in args:
		# 	if room_type == "OF":
		# 		Amity.offices.append(room)
		# 	elif room_type == "LS":
		# 		Amity.offices.append(room)
		# 	else:
		# 		return "Invalid Room Type"

	@staticmethod
	def add_person(**kwargs):
		pass
		# first_name = kwargs.get('first_name', None)
		# last_name = kwargs.get('last_name', None)
		# person_type = kwargs.get('person_type', None) # Person Type: FELLOW, STAFF
		# wants_accomodation = kwargs.get('wants_accomodation', 'N')
		# full_name = first_name.capialize() + " " + last_name.capitalize()

		# if person_type.upper() == "FELLOW":
		# 	Amity.fellows.append(full_name)
		# elif person_type.upper() == "STAFF":
		# 	Amity.staff.append(full_name)
		# else:
		# 	return "Invalid Person Type"

	# Helper Method for allocating rooms randomly
	@staticmethod
	def allocate_random_room(full_name):
		pass
		# all_rooms = Amity.offices + Amity.living_spaces
		# all_rooms = ["Oculus", "Hogwarts", "Valhalla"]
		# if len(all_rooms) > 0:
		# 	random_room = random.choice(all_rooms)
		# else:
		# 	return "No rooms have been created in Amity"

	@staticmethod
	def reallocate_person(person_id, room_name):
		# Amity.room_allocations[room_name] = [full_name]
		pass

	@staticmethod
	def load_people(filename=""):
		return ""

	@staticmethod
	def print_allocations(filename=""):
		return ""

	@staticmethod
	def print_unallocated(filename=""):
		return ""

	@staticmethod
	def print_room(room_name):
		return ""

	@staticmethod
	def save_state():
		pass

	@staticmethod
	def load_state():
		pass
