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

    #Add Song to Room
    def add_song_to_room(self, song):
        self.song_selection.append(song)

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


        



    
    