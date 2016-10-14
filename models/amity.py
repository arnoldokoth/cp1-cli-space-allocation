import db_crud
import pdb
import random

from database_structure import create_database
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
	def create_room(room_type, *rooms_args):
		""" Creates rooms of different types

		Arguments:
		room_type: the type of room; OF - Office, LS - Living Space
		rooms_args: a tuple of room names; ('Oculus', 'Hogwarts')
		"""
		for room in rooms_args[0]:
			if room_type == "OF":
				Amity.offices.append(room)
				current_room = Room(type="OF", name=room)
			elif room_type == "LS":
				Amity.living_spaces.append(room)
				# import pdb; pdb.set_trace()
				current_room = Room(type="LS", name=room)
			else:
				return "Invalid Room Type"

	@staticmethod
	def add_person(**kwargs):
		""" Creates a person with a given classification

		Arguments:
		kwargs: contains the person to be created attributes
		"""
		first_name = kwargs.get('first_name', None)
		last_name = kwargs.get('last_name', None)
		person_type = kwargs.get('person_type', None) # Person Type: FELLOW, STAFF
		wants_accomodation = kwargs.get('wants_accomodation', 'N')
		full_name = first_name.capitalize() + " " + last_name.capitalize()

		if person_type.upper() == "FELLOW":
			Amity.fellows.append(full_name)
			fellow = Fellow(first_name, last_name)
			random_office = Amity.allocate_random_office()

			if Amity.is_at_max_capacity(random_office):
				random_office = Amity.allocate_random_office()
			else:
				if random_office:
					if random_office in Amity.room_allocations.keys():
						Amity.room_allocations[random_office].append(full_name)
						print("Added: " + full_name + " and allocated them to: " + random_office)
					else:
						Amity.room_allocations[random_office] = [full_name]
						print("Added: " + full_name + " and allocated them to: " + random_office)
				else:
					print("No rooms available!")

				if wants_accomodation.upper() == "Y":
					random_livingspace = Amity.allocate_random_living_space()

					if Amity.is_at_max_capacity(random_livingspace):
						random_livingspace = Amity.allocate_random_living_space()
					else:
						if random_livingspace:
							if random_livingspace in Amity.room_allocations.keys():
								Amity.room_allocations[random_livingspace].append(full_name)
								print("Added: " + full_name + " and acllocated them to: " + random_livingspace)
							else:
								Amity.room_allocations[random_livingspace] = [full_name]
								print("Added: " + full_name + " and allocated them to: " + random_livingspace)

				elif wants_accomodation.upper() == "N":
					print("Not allocated living space")	
		elif person_type.upper() == "STAFF":
			Amity.staff.append(full_name)
			staff = Staff(first_name, last_name)
			random_office = Amity.allocate_random_office()

			if Amity.is_at_max_capacity(random_office):
				random_office = Amity.allocate_random_office()
			else:
				if random_office:
					if random_office in Amity.room_allocations.keys():
						Amity.room_allocations[random_office].append(full_name)
						print("Added: " + full_name + " and allocated them to: " + random_office)
					else:
						Amity.room_allocations[random_office] = [full_name]
						print("Added: " + full_name + " and allocated them to: " + random_office)
				else:
					print("No offices available!")

			if wants_accomodation == "Y":
				print("Staff cannot be allocated living spaces!")
		else:
			print("Invalid Person Type")

	@staticmethod
	def allocate_random_office():
		"""Returns a random office from the list of offices """
		all_offices = Amity.offices

		if len(all_offices) > 0:
			random_room = random.choice(all_offices)
			return random_room
		else:
			return False

	@staticmethod
	def allocate_random_living_space():
		""" Returns a random office from the list of offices """
		all_living_spaces = Amity.living_spaces
		
		if len(all_living_spaces) > 0:
			random_room = random.choice(all_living_spaces)
			return random_room
		else:
			return False

	# Helper Method to check if room is a at max capacity
	@staticmethod
	def is_at_max_capacity(room_name):
		""" Returns a boolean """
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

	@staticmethod
	def reallocate_person(full_name, room_name):
		""" Moves someone from one room to another

		Arguments:
		full_name: full_name of person; fellow or staff
		room_name: room person is to be moved to
		"""
		if room_name in Amity.offices + Amity.living_spaces:
			if full_name in Amity.fellows:
				# current person is a fellow so he can be reallocated to both offices & living spaces
				all_rooms = Amity.offices + Amity.living_spaces
				if room_name in Amity.room_allocations.keys():
					for room in Amity.room_allocations.keys():
						if full_name in Amity.room_allocations[room]:
							Amity.room_allocations[room].remove(full_name)
					if Amity.is_at_max_capacity(room_name):
						print("Room already full!")
					else:
						Amity.room_allocations[room_name].append(full_name)
				else:
					Amity.room_allocations[room_name] = [full_name]
			elif full_name in Amity.staff:
				# this guy is staff thus can only be allocated to an office
				all_rooms = Amity.offices
				if room_name in Amity.room_allocations.keys():
					for room in Amity.room_allocations.keys():
						if full_name in Amity.room_allocations[room]:
							Amity.room_allocations[room].remove(full_name)
					if Amity.is_at_max_capacity(room_name):
						print("Room already full!")
					else:
						Amity.room_allocations[room_name].append(full_name)
				else:
					Amity.room_allocations[room_name] = [full_name]
		else:
			print("Room {0} not created!".format(room_name))	

	@staticmethod
	def load_people(filename):
		""" Loads people from the specified file

		Arguments:
		filename: name of file containing data 
		"""
		if filename:
			with open(filename, "r") as file:
				lines = file.readlines()
				for line in lines:
					person_details = line.split()
					if len(person_details) == 3:
						first_name = person_details[0]
						last_name = person_details[1]
						person_type = person_details[2]
						wants_accomodation = "N"
						Amity.add_person(first_name=first_name, last_name=last_name, person_type=person_type, wants_accomodation=wants_accomodation)
					elif len(person_details) == 4:
						first_name = person_details[0]
						last_name = person_details[1]
						person_type = person_details[2]
						wants_accomodation = person_details[3]
						Amity.add_person(first_name=first_name, last_name=last_name, person_type=person_type, wants_accomodation=wants_accomodation)
					else:
						print("could not process provided data!")
		else:
			print("Please provide a file!")

	# Helper Method to convert dictionary keys to a list
	@staticmethod
	def convert_keys_to_list(allocation_keys):
		""" Converts a dictionary's keys from type dict_keys to type list
		
		Arguments:
		allocation_keys: room_allocation keys

		Return:
		output_list: list containing the keys
		"""
		output_list = []
		for item in allocation_keys:
			output_list.append(item)

		return output_list

	@staticmethod
	def print_allocations(filename=""):
		""" Display the currently created rooms and people in them

		Arguments:
		filename: if a filename is provided then this function prints to the file
		"""
		if filename:
			print("\nwriting to file...\n")
			with open(filename, 'w') as file:
				rooms = Amity.convert_keys_to_list(Amity.room_allocations.keys())
				for room in rooms:
					file.write(room.upper() + "\n")
					file.write("-" * 50 + "\n")
					people = Amity.room_allocations[room]
					str_people = ", ".join(people)
					file.write(str_people + "\n")
		else:
			print("\nprinting allocations...\n")
			rooms = Amity.convert_keys_to_list(Amity.room_allocations.keys())
			for room in rooms:
				Amity.print_room(room)
		
	@staticmethod
	def print_unallocated(filename=""):
		""" Display the people currently unallocated

		Arguments:
		filename: if a filename is provided then this function prints to the file
		"""
		all_people = Amity.fellows + Amity.staff
		allocated_people = []
		for room in Amity.room_allocations.keys():
			for person in Amity.room_allocations[room]:
				allocated_people.append(person)
		unallocated_people = [person for person in all_people if person not in allocated_people]
		str_unallocated_people = ", ".join(unallocated_people)

		if filename:
			print("\nwriting to file...\n")
			with open(filename, "w") as file:
				file.write("UNALLOCATED PEOPLE" + "\n")
				file.write("-" * 50 + "\n")
				file.write(str_unallocated_people + "\n")
		else:
			print("printing unallocated...\n")
			print("UNALLOCATED PEOPLE")
			print("-" * 50)
			print(str_unallocated_people)

	@staticmethod
	def print_room(*args):
		""" Prints the people currently allocated to a room

		Arguments:
		args: tuple with room names
		""" 
		for room_name in args:
			room_type = ""
			if room_name in Amity.offices:
				room_type = "Office"
			elif room_name in Amity.living_spaces:
				room_type = "Living Space"	
			if room_name in Amity.convert_keys_to_list(Amity.room_allocations.keys()):
				print(room_name.upper() + " -> " + room_type)
				print("-" * 50)
				people = Amity.room_allocations[room_name]
				str_people = ", ".join(people)
				print(str_people + "\n")
			else:
				print("Room has no allocations or does not exist!")

	@staticmethod
	def save_state(database_name):
		""" Saves the current state of the application to the database

		Arguments:
		database_name: database to be saved to
		"""
		if database_name:
			create_database(database_name)
		else:
			create_database("")

		print(db_crud.save_fellows(Amity.fellows))
		print(db_crud.save_staff(Amity.staff))
		print(db_crud.save_offices(Amity.offices))
		print(db_crud.save_livingspaces(Amity.living_spaces)) 
		print(db_crud.save_allocations(Amity.room_allocations))

	@staticmethod
	def load_state(database_name):
		""" Loads the previously saved state of the application

		Arguments:
		database_name: database to load data from
		"""
		if database_name:
			print("reading data from {0}".format(database_name))
			create_database(database_name)
			Amity.fellows = db_crud.get_all_fellows()
			Amity.staff = db_crud.get_all_staff()
			Amity.offices = db_crud.get_all_offices()
			Amity.living_spaces = db_crud.get_all_livingspaces()
			Amity.room_allocations  = db_crud.get_room_allocations()	
		