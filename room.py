class Room():
    number_of_rooms = 0
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
        Room.number_of_rooms += 1

    # Description test
    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return(self.description)

    def describe(self):
        print(self.description)
    
    # Name test
    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return(self.name)
    
    def show_name(self):
        print(self.name)

    # Link rooms test
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        #print(f"{self.name} linked rooms: {repr(self.linked_rooms)}")
    
    def get_details(self):
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.get_name()} is {direction}.", end=" ")

    def move(self, direction):
        if direction in self.linked_rooms:
            print(f"You go {direction.lower()}.")
            return self.linked_rooms[direction]
        else:
            print(f"You can't go {direction.lower()}!")
            return(self)
    
    # Places characters in rooms
    def set_character(self, character_name):
        self.character = character_name
    
    def get_character(self):
        return self.character
    
    # Places items in rooms
    def set_item(self, item_name):
        self.item = item_name
    
    def get_item(self):
        return self.item