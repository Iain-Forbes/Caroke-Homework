import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Saviour", "Rise Against")
    
    def test_song_has_title(self):
       self.assertEqual("Saviour", self.song.title)

    def test_song_has_artits(self):
        self.assertEqual("Rise Against", self.song.artist)
