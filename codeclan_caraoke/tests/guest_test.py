import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest


class TestGuest(unittest.TestCase):

    #Setup test guest 
    def setUp(self):
        self.guest_1 = Guest("Baron Von Humperdink", 25, 40)
        
    #Test, test guest has name
    def test_guest_name(self):
       self.assertEqual("Baron Von Humperdink", self.guest_1.name)

    #Test, test guest has age
    def test_guest_age(self):
        self.assertEqual(25, self.guest_1.age)

    #Test, test guest has wallet, with cash (40)
    def test_guest_wallet(self):
        self.assertEqual(40, self.guest_1.wallet)

