import unittest

from models.room import Room


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_one = Room(name="Oculus", type="OF")

if __name__ == '__main__':
    unittest.main()
