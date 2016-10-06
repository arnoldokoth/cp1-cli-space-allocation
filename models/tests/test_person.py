import unittest

from models.person import Person

class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person_one = Person("Arnold", "Okoth")

    def test_is_instance_of(self):
        self.assertIsInstance(self.person_one, Person)

    def test_object_property_firstname(self):
        self.assertEqual("Arnold", self.person_one.first_name)

    def test_object_property_lastname(self):
        self.assertEqual("Okoth", self.person_one.last_name)


if __name__ == '__main__':
    unittest.main()
