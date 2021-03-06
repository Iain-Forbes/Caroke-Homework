class Room:

    def __init__(self, room_number, song_selection, total_cash, karoke_cost, room_limit):
        self.room_number = room_number
        self.booked_guest = []
        self.song_selection = song_selection
        self.total_cash = total_cash
        self.karoke_cost = karoke_cost
        self.room_limit = room_limit

    # Check length of Booked List
    def booked_count(self):
        return len(self.booked_guest)

    #Add Guest to Booked List
    def book_room(self, guest): 
        self.booked_guest.append(guest)
    
    #Remove Guest
    def clear_guest(self):
        self.booked_guest.clear()

    #Add Song to Room
    def add_song_to_room(self, song):
        self.song_selection.append(song)
        return self.song_selection

    #Return Total Cash
    def get_cash_total(self):
        return self.total_cash

    #Increase Total Cash by Karoke Machine Cost
    def karoke_machine_charge(self, money_in):
        self.total_cash += money_in

    #Checks there is space in room, if booked_count is less than or equal to room_limit
    def check_room_has_space(self):
        if self.booked_count() <= self.room_limit:
            return True
        else:
            return False

    #Get and store guest favorite song
    def get_guest_fav_song(self, guest):
        return guest.fav_song        

    #Non-working function to woo at fav song
    def woo_at_fave_song(self, guest, song):
        fav_song = self.get_guest_fav_song(guest)
        if fav_song == self.song_selection:
            print ("Wooo")
        else:
            print ("Boo")