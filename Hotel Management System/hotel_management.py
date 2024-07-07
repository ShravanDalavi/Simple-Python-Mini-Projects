import datetime

class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_available = True
        self.guest = None

    def check_in(self, guest):
        if self.is_available:
            self.is_available = False
            self.guest = guest
            return True
        return False

    def check_out(self):
        if not self.is_available:
            self.is_available = True
            self.guest = None
            return True
        return False

    def __str__(self):
        status = 'Available' if self.is_available else f'Occupied by {self.guest.name}'
        return f"Room {self.room_number} ({self.room_type}) - {status}"

class Guest:
    def __init__(self, name, check_in_date, check_out_date):
        self.name = name
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def find_available_room(self, room_type):
        for room in self.rooms:
            if room.room_type == room_type and room.is_available:
                return room
        return None

    def check_in_guest(self, guest, room_type):
        room = self.find_available_room(room_type)
        if room:
            room.check_in(guest)
            return room
        return None

    def check_out_guest(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room.check_out()
        return False

    def show_rooms(self):
        for room in self.rooms:
            print(room)

def main():
    hotel = Hotel("Grand Hotel")

    # Add some rooms
    hotel.add_room(Room(101, "Single", 100))
    hotel.add_room(Room(102, "Double", 150))
    hotel.add_room(Room(103, "Suite", 250))

    while True:
        print("\nWelcome to the Grand Hotel Management System")
        print("1. Show all rooms")
        print("2. Check in guest")
        print("3. Check out guest")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            hotel.show_rooms()
        elif choice == '2':
            name = input("Enter guest name: ")
            check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
            check_out_date = input("Enter check-out date (YYYY-MM-DD): ")
            room_type = input("Enter room type (Single/Double/Suite): ")
            guest = Guest(name, check_in_date, check_out_date)
            room = hotel.check_in_guest(guest, room_type)
            if room:
                print(f"Guest {name} checked into room {room.room_number}")
            else:
                print(f"No available {room_type} rooms")
        elif choice == '3':
            room_number = int(input("Enter room number to check out: "))
            if hotel.check_out_guest(room_number):
                print(f"Room {room_number} is now available")
            else:
                print(f"Room {room_number} is already available or does not exist")
        elif choice == '4':
            print("Thank you for using the Grand Hotel Management System")
            break
        else:
            print("Invalid choice, please try again")

if __name__ == '__main__':
    main()
