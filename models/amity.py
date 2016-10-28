import db_crud
import random

from database_structure import create_database, Base
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
            cls.room_allocations[room] = []
            if room_type == "OF":
                cls.offices.append(room)
                current_room = Room(type="OF", name=room)
                print("Created {0} of type {1}".format(room, "Office"))
            elif room_type == "LS":
                cls.living_spaces.append(room)
                current_room = Room(type="LS", name=room)
                print("Created {0} of type {1}".format(room, "Living Space"))
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
        person_type = kwargs.get('person_type', None)
        wants_accomodation = kwargs.get('wants_accomodation', 'N')
        full_name = first_name.capitalize() + " " + last_name.capitalize()

        # Get a random office
        random_office = cls.allocate_random_office()
        OFFICE_MSG = "OFFICE ALLOCATION"

        # Person Type = Fellow
        if person_type.upper() == "FELLOW":
            cls.fellows.append(full_name)
            if random_office:
                if random_office in cls.room_allocations.keys():
                    cls.room_allocations[random_office].append(full_name)
                else:
                    cls.room_allocations[random_office] = [full_name]
                print("{0}: Added {1} and allocated them to {2}".format(
                    OFFICE_MSG, full_name, random_office
                ))
            else:
                print("{0}: No Office Available!".format(OFFICE_MSG))

            random_livingspace = cls.allocate_random_living_space()
            if wants_accomodation.upper() == "Y":
                MSG = "LIVINGSPACE ALLOCATION"
                if random_livingspace:
                    if random_livingspace in cls.room_allocations.keys():
                        cls.room_allocations[random_livingspace].append(
                            full_name)
                    else:
                        cls.room_allocations[random_livingspace] = [full_name]
                    print("{0}: Added {1} and allocated them to: {2}".format(
                        MSG, full_name, random_livingspace
                    ))
                else:
                    print("{0}: No Living Spaces Available!".format(MSG))
            elif wants_accomodation.upper() == "N":
                print("Not Allocated Living Space!")
        # Person Type = Staff
        elif person_type.upper() == "STAFF":
            cls.staff.append(full_name)
            if random_office:
                if random_office in cls.room_allocations.keys():
                    cls.room_allocations[random_office].append(full_name)
                else:
                    cls.room_allocations[random_office] = [full_name]
                print("{0}: Added {1} and allocated them to: {2}".format(
                    OFFICE_MSG, full_name, random_office
                ))
            else:
                print("{0}: No Offices Available!".format(OFFICE_MSG))

            if wants_accomodation.upper() == "Y":
                print("Staff Cannot be allocated Living Space")
        else:
            print("Invalid Person Type")
        #######################################################################

    @classmethod
    def allocate_random_office(cls):
        """Returns a random office from the list of offices """
        available_offices = [office for office in cls.offices
                             if not cls.is_at_max_capacity(office)]

        if available_offices:
            random_office = random.choice(available_offices)
            return random_office
        else:
            return False

    @classmethod
    def allocate_random_living_space(cls):
        """ Returns a random office from the list of offices """
        available_living_spaces = [livingspace for livingspace in
                                   cls.living_spaces if not
                                   cls.is_at_max_capacity(livingspace)]

        if available_living_spaces:
            random_livingspace = random.choice(available_living_spaces)
            return random_livingspace
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
                return current_capacity == max_capacity
            else:
                return False
        elif room_name in cls.living_spaces:
            max_capacity = 4
            if room_name in cls.room_allocations.keys():
                current_capacity = len(cls.room_allocations[room_name])
                return current_capacity == max_capacity
            else:
                return False

    @classmethod
    def reallocate_person_2(cls, reallocation_type, full_name, room_name):
        """ Moves a person from one room to another

        Arguments:
        full_name: person to be moved
        room_name: room person is to be moved to
        """
        if not cls.is_at_max_capacity(room_name):
            if reallocation_type == "OF":
                if room_name in cls.offices:
                    for room in cls.offices:
                        if full_name in cls.room_allocations[room]:
                            cls.room_allocations[room].remove(full_name)
                    cls.room_allocations[room_name].append(full_name)
                    print("Reallocated {0} to {1}".format(full_name, room_name))
                else:
                    print("Room Does Not Exist!")
            elif reallocation_type == "LS":
                if room_name in cls.living_spaces:
                    for room in cls.living_spaces:
                        if full_name in cls.room_allocations[room]:
                            cls.room_allocations[room].remove(full_name)
                    cls.room_allocations[room_name].append(full_name)
                    print("Reallocated {0} to {1}".format(full_name, room_name))
                else:
                    print("Room Does Not Exist!")
            else:
                print("Invalid Reallocation Flag")
        else:
            print("Room Already Full!")
        #####################################

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
                        cls.add_person(first_name=first_name,
                                       last_name=last_name,
                                       person_type=person_type,
                                       wants_accomodation=wants_accomodation)
                    elif len(person_details) == 4:
                        first_name = person_details[0]
                        last_name = person_details[1]
                        person_type = person_details[2]
                        wants_accomodation = person_details[3]
                        cls.add_person(first_name=first_name,
                                       last_name=last_name,
                                       person_type=person_type,
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
        filename: if a filename is provided then this function prints to the
                  file
        """
        if filename:
            print("\nWRITING TO: {0} \n".format(filename))
            with open(filename, 'w') as file:
                rooms = Amity.convert_keys_to_list(cls.room_allocations.keys())
                for room in rooms:
                    people = cls.room_allocations[room]
                    str_people = ", ".join(people)
                    file_output = room.upper() + "\n"
                    file_output += "-" * 50 + "\n"
                    file_output += str_people + "\n\n"
                    file.write(file_output)
        else:
            print("\nALLOCATIONS\n")
            rooms = Amity.convert_keys_to_list(cls.room_allocations.keys())
            for room in rooms:
                cls.print_room(room)

    @classmethod
    def print_unallocated(cls, filename=""):
        """ Display the people currently unallocated

        Arguments:
        filename: if a filename is provided then this function prints to the
                  file
        """
        all_people = cls.fellows + cls.staff
        allocated_people = []
        for room in cls.room_allocations.keys():
            for person in cls.room_allocations[room]:
                allocated_people.append(person)
        unallocated_people = [person for person in all_people if person not in
                              allocated_people]
        str_unallocated_people = ", ".join(unallocated_people)

        rooms = cls.offices + cls.living_spaces
        unallocated_rooms = [room for room in rooms if room not in
                             cls.room_allocations.keys()]
        str_unallocated_rooms = ", ".join(unallocated_rooms)
        if filename:
            print("\nwriting to file...\n")
            with open(filename, "w") as file:
                file_output = "UNALLOCATED PEOPLE" + "\n"
                file_output += "-" * 50 + "\n"
                file_output += str_unallocated_people + "\n"
                file.write(file_output)
        else:
            print("\nUNALLOCATED PEOPLE\n")
            print("-" * 50)
            print(str_unallocated_people)
            print("\nUNALLOCATED ROOMS\n")
            print("-" * 50)
            print(str_unallocated_rooms)

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
    def save_state(cls, database_name=""):
        engine = None
        save_db = None
        if database_name:
            engine = create_database(database_name)
            save_db = db_crud.Database(engine)
            Base.metadata.create_all(engine)

        print(save_db.save_fellows(cls.fellows))
        print(save_db.save_staff(cls.staff))
        print(save_db.save_offices(cls.offices))
        print(save_db.save_livingspaces(cls.living_spaces))
        print(save_db.save_allocations(cls.room_allocations))

    @classmethod
    def load_state(cls, database_name):
        """ Loads the previously saved state of the application

        Arguments:
        database_name: database to load data from
        """
        engine = None
        load_db = None
        if database_name:
            print("reading data from {0}".format(database_name))
            engine = create_database(database_name)
            load_db = db_crud.Database(engine)
            Base.metadata.create_all(engine)
            cls.fellows = load_db.get_all_fellows()
            cls.staff = load_db.get_all_staff()
            cls.offices = load_db.get_all_offices()
            cls.living_spaces = load_db.get_all_livingspaces()
            cls.room_allocations = load_db.get_room_allocations()
