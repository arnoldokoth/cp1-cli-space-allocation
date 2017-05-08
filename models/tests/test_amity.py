import os
import unittest

from models.amity import Amity


class TestAmity(unittest.TestCase):
    def setUp(self):
        Amity.offices = []
        Amity.living_spaces = []
        Amity.staff = []
        Amity.fellows = []
        Amity.room_allocations = {}
        self.load_people_file = "test_load_people.txt"
        self.allocations_file = "test_allocated_rooms.txt"
        self.unallocated_rooms_file = "test_unallocated_rooms.txt"

        with open(self.load_people_file, "w") as f:
            f.write("OLUWAFEMI SULE FELLOW Y\nDOMINIC WALTERS STAFF\n\
                     SIMON PATTERSON FELLOW Y\nMARI LAWRENCE FELLOW Y\n\
                     LEIGH RILEY STAFF\nTANA LOPEZ FELLOW Y\n\
                     KELLY McGUIRE STAFF\n")

        with open(self.allocations_file, "w") as f:
            f.write("Oculus ------- Arnold Okoth")

        with open(self.unallocated_rooms_file, "w") as f:
            f.write("Hogwarts")

    def tearDown(self):
        try:
            os.remove(self.load_people_file)
            os.remove(self.allocations_file)
            os.remove(self.unallocated_rooms_file)
            os.remove("test.db")
        except Exception:
            print("error deleting test files")

    def test_create_office(self):
        offices = ["Oculus", "Krypton"]
        Amity.create_room("OF", offices)
        self.assertIn("Oculus", Amity.offices)
        self.assertIn("Krypton", Amity.offices)

    def test_create_livingspace(self):
        living_spaces = ["Java", "PHP"]
        Amity.create_room("LS", living_spaces)
        self.assertIn("Java", Amity.living_spaces)
        self.assertIn("PHP", Amity.living_spaces)

    def test_add_fellows(self):
        Amity.add_person(first_name="Arnold", last_name="Okoth",
                         person_type="Fellow")
        Amity.add_person(first_name="Kristina", last_name="Novelli",
                         person_type="Fellow")
        self.assertIn("Arnold Okoth", Amity.fellows)
        self.assertIn("Kristina Novelli", Amity.fellows)

    def test_add_staff(self):
        Amity.add_person(first_name="Mark", last_name="Manson",
                         person_type="Staff")
        Amity.add_person(first_name="Jimmy", last_name="Kamau",
                         person_type="Staff")
        self.assertIn("Mark Manson", Amity.staff)
        self.assertIn("Jimmy Kamau", Amity.staff)

    def test_load_people(self):
        # Read from the file created in setUp: load_people_file
        offices = ["Oculus"]
        living_spaces = ["Java"]
        Amity.create_room("OF", offices)
        Amity.create_room("LS", living_spaces)
        Amity.load_people(self.load_people_file)
        self.assertIn("Oluwafemi Sule", Amity.fellows)
        self.assertIn("Dominic Walters", Amity.staff)

    def test_room_allocation(self):
        offices = ["Oculus"]
        living_spaces = ["Java"]
        Amity.create_room("OF", offices)
        Amity.create_room("LS", living_spaces)
        Amity.add_person(first_name="Arnold", last_name="Okoth",
                         person_type="Staff")
        Amity.add_person(first_name="Emma", last_name="Hewitt",
                         person_type="Fellow", wants_accomodation="Y")
        self.assertIn("Arnold Okoth", Amity.room_allocations["Oculus"])
        self.assertIn("Emma Hewitt", Amity.room_allocations["Java"])

    # @unittest.skip("work in progress")
    def test_reallocate_person(self):
        Amity.create_room("OF", ["Oculus"])
        Amity.add_person(first_name="Arnold", last_name="Okoth",
                         person_type="Staff")
        self.assertIn("Arnold Okoth", Amity.room_allocations["Oculus"])
        Amity.create_room("OF", ["Narnia"])
        Amity.reallocate_person_2("OF", "Arnold Okoth", "Narnia")
        self.assertIn("Arnold Okoth", Amity.room_allocations["Narnia"])

    def test_save_and_load_state(self):
        offices = ["Oculus", "Narnia"]
        living_spaces = ["Java", "PHP"]
        Amity.create_room("OF", offices)
        Amity.create_room("LS", living_spaces)
        Amity.load_people(self.load_people_file)
        Amity.save_state("test.db")
        print("Loading State")
        Amity.load_state("test.db")
        self.assertIn("Simon Patterson", Amity.fellows)

if __name__ == '__main__':
    unittest.main()
