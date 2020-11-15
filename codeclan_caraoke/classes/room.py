class Room:

    def __init__(self, room_number, song_selection):
        self.room_number = room_number
        self.booked_guest = []
        self.song_selection = song_selection

    # Check length of Booked List
    def booked_count(self):
        return len(self.booked_guest)

    #Add Guest to Booked List
    def book_room(self, guest): 
        self.booked_guest.append(guest)

    #Add Song to Room
    def add_song_to_room(self, song):
        self.song_selection.append(song)

    #Charge Guest to use Karoke Machine 
    def karoke_cost(self, cash):
        pass



    
    