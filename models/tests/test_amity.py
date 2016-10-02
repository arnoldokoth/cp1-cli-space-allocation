import unittest

from models.amity import Amity

class TestAmity(unittest.TestCase):

    def setUp(self):
        self.amity_object = Amity()

    def test_is_instance_of(self):
        self.assertIsInstance(self.amity_object, Amity)

    @unittest.skip("work in progress")
    def test_create_room(self):
        pass

    @unittest.skip("work in progress")
    def test_add_person(self):
        pass

    @unittest.skip("work in progress")
    def test_reallocate_person(self):
        pass

    @unittest.skip("work in progress")
    def test_load_people(self):
        pass

    @unittest.skip("work in progress")
    def test_print_allocations(self):
        pass

    @unittest.skip("work in progress")
    def test_print_room(self):
        pass

    @unittest.skip("work in progress")
    def test_save_state(self):
        pass

    @unittest.skip("work in progress")
    def test_load_state(self):
        pass


if __name__ == '__main__':
    unittest.main()
