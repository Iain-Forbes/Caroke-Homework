import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest


class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Baron Von Humperdink", 17)
        self.guest_2 = Guest("Sir Hamalot", 43)
        
    def test_guest_name_and_age(self):
       self.assertEqual("Baron Von Humperdink", self.guest_1.name)

    def test_guest_age(self):
        self.assertEqual(17, self.guest_1.age)
