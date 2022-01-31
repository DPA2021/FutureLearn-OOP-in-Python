class Item():
    def __init__(self, item_name) -> None:
        self.name = item_name
        self.interpretation = None

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, item_name):
        self._name = item_name

    @property
    def interpretation(self):
        return self._interpretation
    
    @interpretation.setter
    def interpretation(self, item_interpretation):
        self._interpretation = item_interpretation

    # Describes item in room
    def see_item(self):
        if (self.name[0].lower() == "a" or self.name[0].lower() == "e" or self.name[0].lower() == "i" or
        self.name[0].lower() == "o" or self.name[0].lower() == "u"):
            print(f"There is an {self.name.lower()} in the room.", end=" ")
            print(f"{self.interpretation}")
        else:
            print(f"There is a {self.name.lower()} in the room.", end=" ")
            print(f"{self.interpretation}")
    
    # Adds items to backpack
    def collect(self, backpack, current_room):
        backpack.append(self.name)
        print(f"You put the {self.name} inside your trusty backpack.")
        current_room.set_item(None)