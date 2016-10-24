import unittest

from models.room import Room

class TestRoom(unittest.TestCase):

	def setUp(self):
		self.room_one = Room("Oculus")

	def test_is_instance_of(self):
		self.assertIsInstance(self.room_one, Room)

	def test_object_property_name(self):
		self.assertEqual(self.room_one.name, "Oculus")

if __name__ == '__main__':
	unittest.main()