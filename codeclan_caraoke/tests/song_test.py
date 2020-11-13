import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestSong(unittest.TestCase):
    pass

    def setUp(self):
        self.playlist = {
        "Title_1": "Saviour", "Artist_1": "Rise Against",
        "Title_2": "Blitzkrieg Bop", "Artist_2": "Ramones",
        "Title_3": "Faith Alone", "Artist_3": "Bad Religion"
        }

    def test_song_has_title(self):
        self.assertEqual("Saviour", self.playlist["Title_1"])

    def test_song_has_artist(self):
        self.assertEqual("Rise Against", self.playlist["Artist_1"])

    def test_play_list_count(self):
        self.assertEqual(3, self.playlist[Keys])