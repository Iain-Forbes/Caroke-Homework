import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Karoke Room 1", "Saviour")
        self.guest = Guest("Baron Humperdink", 17)
        self.song_1 =  Song("Saviour",  "Rise Against")

    def test_check_room_number(self):
        self.assertEqual("Karoke Room 1", self.room.room_number)
        
    def test_room_starts_unbooked(self):
        self.assertEqual(0, self.room.booked_count())

    def test_room_booking(self):
        self.room.book_room(self.guest)
        self.assertEqual(1, self.room.booked_count())
        
    def test_add_song_to_room(self):
        self.assertEqual(self.room.song_selection, "Saviour")
 
        

