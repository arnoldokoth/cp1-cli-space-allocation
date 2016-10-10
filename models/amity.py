import pdb
import random

from models.staff import Staff
from models.fellow import Fellow
from models.room import Room


class Amity:

	# Application Data 
	offices = []
	living_spaces = []
	fellows = []
	staff = []
	room_allocations = {}


	@staticmethod
	def create_room(room_type, *args):
		""" Creates rooms in the application
		"""
		for room in args:
			if room_type == "OF":
				Amity.offices.append(room)
				current_room = Room(type="OF", name=room)
			elif room_type == "LS":
				Amity.living_spaces.append(room)
				current_room = Room(type="LS", name=room)
			else:
				return "Invalid Room Type"


	@staticmethod
	def add_person(**kwargs):
		# Assign Person Attributes
		first_name = kwargs.get('first_name', None)
		last_name = kwargs.get('last_name', None)
		person_type = kwargs.get('person_type', None) # Person Type: FELLOW, STAFF
		wants_accomodation = kwargs.get('wants_accomodation', 'N')
		full_name = first_name.capitalize() + " " + last_name.capitalize()

		# Create person of fellow
		if person_type.upper() == "FELLOW":
			Amity.fellows.append(full_name)
			fellow = Fellow(first_name, last_name)
		elif person_type.upper() == "STAFF":
			Amity.staff.append(full_name)
			staff = Staff(first_name, last_name)
		else:
			return "Invalid Person Type"

		if wants_accomodation == "Y":
			random_room = Amity.allocate_random_room(person_type)

			if Amity.is_at_max_capacity(random_room):
				random_room = Amity.allocate_random_room(person_type)

			if random_room in Amity.room_allocations.keys():
				Amity.room_allocations[random_room].append(full_name)
				return "Added: " + full_name + " and allocated them to: " + random_room
			else:
				Amity.room_allocations[random_room] = [full_name]
				return "Added: " + full_name + " and allocated them to: " + random_room
		elif wants_accomodation == "N":
			return "Added: " + full_name


	# Helper Method to check if room is a at max capacity
	@staticmethod
	def is_at_max_capacity(room_name):
		if room_name in Amity.offices:
			max_capacity = 6 
			# Check if the room already has some allocations
			if room_name in Amity.room_allocations.keys():
				current_capacity = len(Amity.room_allocations[room_name])
				if current_capacity == max_capacity:
					return True
				else:
				 	return False
		elif room_name in Amity.living_spaces:
			max_capacity = 4
			if room_name in Amity.room_allocations.keys():
				current_capacity = len(Amity.room_allocations[room_name])
				if current_capacity == max_capacity:
					return True
				else:
					return False

					
	# Helper Method for allocating rooms randomly
	@staticmethod
	def allocate_random_room(person_type):
		all_rooms = []
		if person_type.upper() == "FELLOW":
			all_rooms = Amity.offices + Amity.living_spaces
		elif person_type.upper() == "STAFF":
			all_rooms = Amity.offices

		if len(all_rooms) > 0:
			random_room = random.choice(all_rooms)
			return random_room
		else:
			return "No rooms have been created in Amity"


	@staticmethod
	def reallocate_person(full_name, room_name):
		if room_name in Amity.room_allocations.keys():
			pass
		else:
			pass


	@staticmethod
	def load_people(filename=""):
		return ""


	# Helper Method to convert dictionary keys to a list
	@staticmethod
	def convert_keys_to_list(allocation_keys):
		output_list = []
		for item in allocation_keys:
			output_list.append(item)

		return output_list


	@staticmethod
	def print_allocations(filename=""):
		if filename:
			print("writing to file...")
			with open(filename, 'w') as file:
				rooms = Amity.convert_keys_to_list(Amity.room_allocations.keys())
				for room in rooms:
					file.write(room.upper() + "\n")
					file.write("-" * 50 + "\n")
					people = Amity.room_allocations[room]
					str_people = ", ".join(people)
					file.write(str_people + "\n")
		else:
			print("printing allocations...")
			rooms = Amity.convert_keys_to_list(Amity.room_allocations.keys())
			for room in rooms:
				Amity.print_room(room)
		

	@staticmethod
	def print_unallocated(filename=""):
		if filename:
			print("writing to file...")
		else:
			print("printing unallocated...")
			all_people = Amity.fellows + Amity.staff
			allocated_people = []
			for room in Amity.room_allocations.keys():
				allocated_people = Amity.room_allocations[room]
			print("all people...")
			print(all_people)
			print()
			print("allocated people...")
			print(allocated_people)


	@staticmethod
	def print_room(*args):
		for room_name in args:	
			if room_name in Amity.convert_keys_to_list(Amity.room_allocations.keys()):
				print(room_name.upper())
				print("-" * 50)
				people = Amity.room_allocations[room_name]
				str_people = ", ".join(people)
				print(str_people)
				print()
			else:
				return "Room has no allocations or does not exist!"


	@staticmethod
	def save_state():
		pass


	@staticmethod
	def load_state():
		pass



def test_stuff():
	# Random Testing Stuff
	Amity.create_room("LS", "Oculus", "Valhalla")
	# print(Amity.living_spaces)
	Amity.create_room("OF", "Hogwarts")

	Amity.add_person(first_name="Emma", last_name="Bale", person_type="Fellow", wants_accomodation="Y")
	Amity.add_person(first_name="Lost", last_name="Frequencies", person_type="Staff", wants_accomodation="Y")
	Amity.add_person(first_name="Leona", last_name="Lewis", person_type="Staff", wants_accomodation="Y")
	Amity.add_person(first_name="Arnold", last_name="Okoth", person_type="Fellow", wants_accomodation="N")

	print()
	print("print_room".upper())
	print("#" * 60)
	Amity.print_room("Hogwarts", "Oculus", "Valhalla")
	print("#" * 60)
	print()

	# print("print_allocations".upper())
	# Amity.print_allocations("test.txt")
	Amity.print_unallocated()
	# print()
	# print(type(Amity.room_allocations.keys()))

test_stuff()