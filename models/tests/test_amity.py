import unittest
import os

from models.amity import Amity


class TestAmity(unittest.TestCase):
    def setUp(self):
        self.load_people_file = "test_load_people.txt"
        self.allocations_file = "test_allocated_rooms.txt"
        self.unallocated_rooms_file = "test_unallocated_rooms.txt"

        with open(self.load_people_file, "w") as f:
            f.write("OLUWAFEMI SULE FELLOW Y")

        with open(self.allocations_file, "w") as f:
            f.write("Oculus ------- Arnold Okoth")

        with open(self.unallocated_rooms_file, "w") as f:
            f.write("Hogwarts")

    def tearDown(self):
        try:
            os.remove(self.load_people_file)
            os.remove(self.allocations_file)
            os.remove(self.unallocated_rooms_file)
        except Exception:
            print("error deleting test files")

    def test_create_office(self):
        Amity.create_room("OF", "Oculus")
        self.assertIn("Oculus", Amity.offices)

    def test_create_livingspace(self):
        Amity.create_room("LS", "Narnia")
        self.assertIn("Narnia", Amity.living_spaces)

    def test_add_fellow(self):
        Amity.add_person(first_name="Arnold", last_name="Okoth", person_type="Fellow", wants_accomodation="Y")
        self.assertIn("Arnold Okoth", Amity.fellows)

    def test_add_staff(self):
        Amity.add_person(first_name="Test", last_name="Staff", person_type="Staff", wants_accomodation="N")
        self.assertIn("Test Staff", Amity.staff)

    def test_reallocate_person(self):
        Amity.add_person(first_name="Arnold", last_name="Okoth", person_type="Staff")
        Amity.create_room("OF", "Oculus")
        Amity.reallocate_person("Arnold Okoth", "Oculus")
        self.assertIn("Arnold Okoth", Amity.room_allocations["Oculus"])

    def test_load_people(self):
        # Read from the file created in setUp: load_people_file
        Amity.create_room("OF", "Oculus")
        Amity.create_room("LS", "Hogwarts")
        self.assertIn("OLUWAFEMI SULE", Amity.fellows)

    def test_print_allocations(self):
        Amity.add_person(first_name="Arnold", last_name="Okoth", person_type="Fellow", wants_accomodation="Y")
        self.assertIn("Arnold Okoth Oculus", Amity.print_allocations(self.allocations_file))

    def test_print_unallocated_to_file(self):
        Amity.add_person(first_name="Arnold", last_name="Okoth", person_type="Fellow", wants_accomodation="N")
        self.assertIn("Hogwarts", Amity.print_unallocated(self.unallocated_rooms_file))

    def test_room_allocation(self):
        Amity.add_person(first_name="Arnold", last_name="Okoth", person_type="Staff")
        Amity.create_room("OF", "Oculus")
        Amity.reallocate_person("Arnold Okoth", "Oculus")
        self.assertIn("Arnold Okoth", Amity.room_allocations["Oculus"])


if __name__ == '__main__':
    unittest.main()
