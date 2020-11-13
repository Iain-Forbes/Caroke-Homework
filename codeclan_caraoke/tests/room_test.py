import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Karoke Room 1")
        self.guest = Guest("Baron Humperdink", 17)

    def test_room_starts_unbooked(self):
        self.assertEqual(0, self.room.booked_count())

    def test_room_booking(self):
        self.room.book_room(self.guest)
        self.assertEqual(1, self.room.booked_count())
        

 
        

