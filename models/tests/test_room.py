import unittest

from models.room import Room


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_one = Room(name="Oculus", type="OF")

    def test_room_property_name(self):
        self.assertEqual(self.room_one.name, "Oculus")

if __name__ == '__main__':
    unittest.main()
