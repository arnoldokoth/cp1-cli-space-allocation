import unittest

from models.fellow import Fellow
from models.person import Person

class TestFellow(unittest.TestCase):

    def setUp(self):
        self.fellow_one = Fellow("Arnold", "Okoth", "Male")

    def test_is_subclass(self):
        self.assertTrue(issubclass(Fellow, Person))


if __name__ == '__main__':
    unittest.main()
