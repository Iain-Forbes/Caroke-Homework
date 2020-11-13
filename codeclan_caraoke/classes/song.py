class Song:

    def __init__(self, title, artist, playlist):
        self.title = title
        self.artist = artist
        self.playlist = playlist
        
   
    def show_song_list(self):
        return len(self.playlist)

    def song_selector(self):
        for song in self.playlist:
            if self.playlist == "name":
                return song
        