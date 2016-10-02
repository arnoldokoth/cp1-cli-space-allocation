import unittest

from fellow.fellow import Fellow
from person.person import Person

class TestFellow(unittest.TestCase):

    def setUp(self):
        self.fellow_one = Fellow()

    def test_is_subclass(self):
        self.assertTrue(Fellow issubclass(Person))


if __name__ == '__main__':
    unittest.main()
