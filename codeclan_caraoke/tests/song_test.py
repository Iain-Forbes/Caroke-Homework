import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 =  Song("Saviour",  "Rise Against")
        self.song_2 =  Song("Blitzkrieg Bop",  "Ramones")
        self.song_3 =  Song("Faith Alone",  "Bad Religion")

    def test_song_has_title(self):
        self.assertEqual("Saviour", self.song_1.title)

    def test_song_has_artist(self):
        self.assertEqual("Bad Religion", self.song_3.artist)