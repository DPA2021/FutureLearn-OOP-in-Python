class Character():
    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print(" ")
        print(f"{self.name} is here!", end = " ")
        print(f"{self.description}")

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True
    

class Enemy(Character):
    number_of_enemies = 0
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        Enemy.number_of_enemies += 1
    
    def set_weakness(self, weakness):
        self.weakness = weakness
    
    def get_weakness(self):
        print(f"{self.name} is weak to {self.weakness}!")
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item.lower() == self.weakness.lower():
            print(f"You fend {self.name} with the {combat_item.lower()}.")
            return True
        else:
            print(f"{self.name} cruses you, puny adventurer!")
            return False
    
    def enemy_defeated(self, current_room):
        current_room.set_character(None)
        Enemy.number_of_enemies -= 1


class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
    
    def fight(self):
        print(f"{self.name} doesn't seem to be interested in a fight with you in the slightest.")