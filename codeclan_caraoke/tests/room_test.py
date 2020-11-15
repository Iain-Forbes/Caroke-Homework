import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Karoke Room 1", "Saviour", 0, 3, 2)
        self.guest_1 = Guest("Baron Humperdink", 25, 40)
        self.guest_2 = Guest("Baron Von Jon", 45, 40)
        self.guest_3 = Guest("Baron Steve", 65, 40)
        self.song_1 =  Song("Saviour",  "Rise Against")
     
    #Test room has name 
    def test_check_room_number(self):
        self.assertEqual("Karoke Room 1", self.room.room_number)
        
    #Test room starts with no guests
    def test_room_starts_unbooked(self):
        self.assertEqual(0, self.room.booked_count())

    #Test booking function adds guest to room 
    def test_room_booking(self):
        self.room.book_room(self.guest_1)
        self.assertEqual(1, self.room.booked_count())
        
    #Test song is added to room 
    def test_add_song_to_room(self):
        self.assertEqual(self.room.song_selection, "Saviour")

    #Test room has cash, starts at 0
    def test_room_has_cash(self):
        self.assertEqual(self.room.total_cash, 0)

    #Test that Karoke machine takes £3 and adds to total cash.
    def test_karoke_machine_charge(self):
        self.room.karoke_machine_charge(self.room.karoke_cost)
        self.assertEqual(3, self.room.total_cash)

    #Charges guest, takes £3 from wallet 
    def test_guest_charged(self):
        self.guest_1.charge_guest(self.room.karoke_cost)
        self.assertEqual(37, self.guest_1.wallet)

    #Tests max capcity of each room is 2 
    def test_room_has_capacity_limit(self):
        self.assertEqual(2, self.room.room_limit)
        
    #Test room has Space(Space)
    def test_room_has_space(self):
        self.room.book_room(self.guest_1)
        self.room.book_room(self.guest_2)
        self.assertEqual(True, self.room.check_room_has_space())

    #Test room has Space(No Space)
    def test_room_has_space_fail(self):
        self.room.book_room(self.guest_1)
        self.room.book_room(self.guest_2)
        self.room.book_room(self.guest_3)
        self.assertEqual(False, self.room.check_room_has_space())

  

   
        

