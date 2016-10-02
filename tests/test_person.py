import unittest

from person.person import Person

class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person_one = Person("Arnold", "Okoth", "Male")

    def test_is_instance_of(self):
        self.assertIsInstance(self.person_one, Person)

    def test_is_object_of(self):
        self.assertTrue(type(self.person_one) is Person)

    def test_object_property_firstname(self):
        self.assertEqual("Arnold", self.person_one.first_name)

    def test_object_property_lastname(self):
        self.assertEqual("Okoth", self.person_one.last_name)

    def test_object_property_sex(self):
        self.assertEqual("Male", self.person_one.sex)


if __name__ == '__main__':
    unittest.main()
