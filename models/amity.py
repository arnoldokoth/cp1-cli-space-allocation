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

    @classmethod
    def create_room(cls, room_type, rooms_args):
        """ Creates rooms of different types

		Arguments:
		room_type: the type of room; OF - Office, LS - Living Space
		rooms_args: a tuple of room names; ('Oculus', 'Hogwarts')
		"""
        for room in rooms_args:
            if room_type == "OF":
                cls.offices.append(room)
                current_room = Room(type="OF", name=room)
            elif room_type == "LS":
                cls.living_spaces.append(room)
                current_room = Room(type="LS", name=room)
            else:
                return "Invalid Room Type"

    @classmethod
    def add_person(cls, **kwargs):
        """ Creates a person with a given classification

		Arguments:
		kwargs: contains the person to be created attributes
		"""
        first_name = kwargs.get('first_name', None)
        last_name = kwargs.get('last_name', None)
        person_type = kwargs.get('person_type', None)  # Person Type: FELLOW, STAFF
        wants_accomodation = kwargs.get('wants_accomodation', 'N')
        full_name = first_name.capitalize() + " " + last_name.capitalize()

        if person_type.upper() == "FELLOW":
            cls.fellows.append(full_name)
            fellow = Fellow(first_name, last_name)
            random_office = cls.allocate_random_office()

            if cls.is_at_max_capacity(random_office):
                random_office = cls.allocate_random_office()
            else:
                if random_office:
                    if random_office in cls.room_allocations.keys():
                        cls.room_allocations[random_office].append(full_name)
                        print("Added: " + full_name + " and allocated them to: " + random_office)
                    else:
                        cls.room_allocations[random_office] = [full_name]
                        print("Added: " + full_name + " and allocated them to: " + random_office)
                else:
                    print("No rooms available!")

                if wants_accomodation.upper() == "Y":
                    random_livingspace = cls.allocate_random_living_space()

                    if cls.is_at_max_capacity(random_livingspace):
                        random_livingspace = cls.allocate_random_living_space()
                    else:
                        if random_livingspace:
                            if random_livingspace in cls.room_allocations.keys():
                                cls.room_allocations[random_livingspace].append(full_name)
                                print("Added: " + full_name + " and acllocated them to: " + random_livingspace)
                            else:
                                cls.room_allocations[random_livingspace] = [full_name]
                                print("Added: " + full_name + " and allocated them to: " + random_livingspace)

                elif wants_accomodation.upper() == "N":
                    print("Not allocated living space")
        elif person_type.upper() == "STAFF":
            cls.staff.append(full_name)
            staff = Staff(first_name, last_name)
            random_office = cls.allocate_random_office()

            if cls.is_at_max_capacity(random_office):
                random_office = cls.allocate_random_office()
            else:
                if random_office:
                    if random_office in cls.room_allocations.keys():
                        cls.room_allocations[random_office].append(full_name)
                        print("Added: " + full_name + " and allocated them to: " + random_office)
                    else:
                        cls.room_allocations[random_office] = [full_name]
                        print("Added: " + full_name + " and allocated them to: " + random_office)
                else:
                    print("No offices available!")

            if wants_accomodation == "Y":
                print("Staff cannot be allocated living spaces!")
        else:
            print("Invalid Person Type")

    @classmethod
    def allocate_random_office(cls):
        """Returns a random office from the list of offices """
        all_offices = cls.offices

        if len(all_offices) > 0:
            random_room = random.choice(all_offices)
            return random_room
        else:
            return False

    @classmethod
    def allocate_random_living_space(cls):
        """ Returns a random office from the list of offices """
        all_living_spaces = cls.living_spaces

        if len(all_living_spaces) > 0:
            random_room = random.choice(all_living_spaces)
            return random_room
        else:
            return False

    # Helper Method to check if room is a at max capacity
    @classmethod
    def is_at_max_capacity(cls, room_name):
        """ Returns a boolean """
        if room_name in cls.offices:
            max_capacity = 6
            # Check if the room already has some allocations
            if room_name in cls.room_allocations.keys():
                current_capacity = len(cls.room_allocations[room_name])
                if current_capacity == max_capacity:
                    return True
                else:
                    return False
        elif room_name in cls.living_spaces:
            max_capacity = 4
            if room_name in cls.room_allocations.keys():
                current_capacity = len(cls.room_allocations[room_name])
                if current_capacity == max_capacity:
                    return True
                else:
                    return False

    @classmethod
    def reallocate_person(cls, full_name, room_name):
        """ Moves a person from one room to another

		Arguments:
		full_name: full_name of person; fellow or staff
		room_name: room person is to be moved to
		"""
        if room_name in cls.offices + cls.living_spaces:
            if full_name in cls.fellows:
                # current person is a fellow so he can be reallocated to both offices & living spaces
                all_rooms = cls.offices + cls.living_spaces
                for room in cls.room_allocations.keys():
                    if full_name in cls.room_allocations[room]:
                        cls.room_allocations[room].remove(full_name)
                if cls.is_at_max_capacity(room_name):
                    print("Room already full!")
                else:
                	if room_name in cls.room_allocations.keys():
                		cls.room_allocations[room_name].append(full_name)
                	else:
                		cls.room_allocations[room_name] = [full_name]
            elif full_name in cls.staff:
                # this guy is staff thus can only be allocated to an office
                all_rooms = cls.offices
                for room in cls.room_allocations.keys():
                    if full_name in cls.room_allocations[room]:
                        cls.room_allocations[room].remove(full_name)
                if cls.is_at_max_capacity(room_name):
                    print("Room already full!")
                else:
                	if room_name in cls.room_allocations.keys():
                		cls.room_allocations[room_name].append(full_name)
                	else:
                		cls.room_allocations[room_name] = [full_name]
        else:
            print("Room {0} not created!".format(room_name))

    @classmethod
    def load_people(cls, filename):
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
                        cls.add_person(first_name=first_name, last_name=last_name, person_type=person_type,
                                         wants_accomodation=wants_accomodation)
                    elif len(person_details) == 4:
                        first_name = person_details[0]
                        last_name = person_details[1]
                        person_type = person_details[2]
                        wants_accomodation = person_details[3]
                        cls.add_person(first_name=first_name, last_name=last_name, person_type=person_type,
                                         wants_accomodation=wants_accomodation)
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

    @classmethod
    def print_allocations(cls, filename=""):
        """ Display the currently created rooms and people in them

		Arguments:
		filename: if a filename is provided then this function prints to the file
		"""
        if filename:
            print("\nwriting to file...\n")
            with open(filename, 'w') as file:
                rooms = Amity.convert_keys_to_list(cls.room_allocations.keys())
                for room in rooms:
                    file.write(room.upper() + "\n")
                    file.write("-" * 50 + "\n")
                    people = cls.room_allocations[room]
                    str_people = ", ".join(people)
                    file.write(str_people + "\n")
        else:
            print("\nprinting allocations...\n")
            rooms = Amity.convert_keys_to_list(cls.room_allocations.keys())
            for room in rooms:
                cls.print_room(room)

    @classmethod
    def print_unallocated(cls, filename=""):
        """ Display the people currently unallocated

		Arguments:
		filename: if a filename is provided then this function prints to the file
		"""
        all_people = cls.fellows + cls.staff
        allocated_people = []
        for room in cls.room_allocations.keys():
            for person in cls.room_allocations[room]:
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

    @classmethod
    def print_room(cls, *args):
        """ Prints the people currently allocated to a room

		Arguments:
		args: tuple with room names
		"""
        for room_name in args:
            room_type = ""
            if room_name in cls.offices:
                room_type = "Office"
            elif room_name in cls.living_spaces:
                room_type = "Living Space"
            if room_name in cls.convert_keys_to_list(cls.room_allocations.keys()):
                print(room_name.upper() + " -> " + room_type)
                print("-" * 50)
                people = cls.room_allocations[room_name]
                str_people = ", ".join(people)
                print(str_people + "\n")
            else:
                print("Room has no allocations or does not exist!")

    @classmethod
    def save_state(cls, database_name):
        """ Saves the current state of the application to the database

		Arguments:
		database_name: database to be saved to
		"""

        print(db_crud.save_fellows(cls.fellows))
        print(db_crud.save_staff(cls.staff))
        print(db_crud.save_offices(cls.offices))
        print(db_crud.save_livingspaces(cls.living_spaces))
        print(db_crud.save_allocations(cls.room_allocations))

    @classmethod
    def load_state(cls, database_name):
        """ Loads the previously saved state of the application

		Arguments:
		database_name: database to load data from
		"""
        if database_name:
            print("reading data from {0}".format(database_name))
            create_database(database_name)
            cls.fellows = db_crud.get_all_fellows()
            cls.staff = db_crud.get_all_staff()
            cls.offices = db_crud.get_all_offices()
            cls.living_spaces = db_crud.get_all_livingspaces()
            cls.room_allocations = db_crud.get_room_allocations()
