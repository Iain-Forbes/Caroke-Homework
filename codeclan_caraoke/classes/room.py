class Room:

    def __init__(self, room_number):
        self.room_number = room_number
        self.booked_guest = []

    def booked_count(self):
        return len(self.booked_guest)

    def book_room(self, guest): 
        self.booked_guest.append(guest)

    
    