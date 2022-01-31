from room import Room
from item import Item
from character import Enemy, Friend
from rpginfo import RPGInfo
from time import sleep

def main():
    # Welcomes the player
    spooky_castle = RPGInfo("The Old Mansion Cleanup")
    spooky_castle.welcome()
    RPGInfo.info()
    
    RPGInfo.author = "Pablo Diaz"
    RPGInfo.credits()
    print(" ")
    print("Press Enter to begin.")
    input("")

    # Initializes rooms
    main_hall = Room("main_hall")
    main_hall.set_name("Grand Main Hall")
    main_hall.set_description("Despite being long abandoned, this hall remains grand and imposing.")

    upper_main_hall = Room("upper_main_hall")
    upper_main_hall.set_name("Upper Main Hall")
    upper_main_hall.set_description("The deteriorated yet opulent stairway splits into east and west.")

    kitchen = Room("kitchen")
    kitchen.set_name("Abandoned Kitchen")
    kitchen.set_description("A dank and dirty room buzzing with flies.")

    ballroom = Room("ballroom")
    ballroom.set_name("Worn-out Ballroom")
    ballroom.set_description("An old and dusty ballroom filled with cracks and insects.")

    dining_hall = Room("dining_hall")
    dining_hall.set_name("Dining Hall")
    dining_hall.set_description("The remains of a luxurious and classy dining room.")

    art_gallery = Room("art_gallery")
    art_gallery.set_name("Disarrayed Art Gallery")
    art_gallery.set_description("Old paintings and shattered sculptures decorate the dim lit room.")

    storeroom = Room("storeroom")
    storeroom.set_name("Vast Storeroom")
    storeroom.set_description("A large storage room now inhabited by a bunch of spiders.")

    bedroom = Room("bedroom")
    bedroom.set_name("Broken-down Bedroom")
    bedroom.set_description("A very messy room with sheets and clothes all over.")

    bathroom = Room("bathroom")
    bathroom.set_name("Ornate Bathroom")
    bathroom.set_description("Surprisingly, this is the cleanest room you've seen thus far.")

    garden = Room("garden")
    garden.set_name("Labyrinthian Garden")
    garden.set_description("The gardens are big and very confusing. There is a hedge maze to the north.")

    hedge_maze = Room("hedge_maze")
    hedge_maze.set_name("Hedge Maze")
    hedge_maze.set_description("You may get lost for an hour or two if you're not careful.")

    stable = Room("stable")
    stable.set_name("Large Stable")
    stable.set_description("Not a single horse in sight unfortunately.")

    overlook = Room("overlook")
    overlook.set_name("Garden Overlook")
    overlook.set_description("The view of this place would be amazing if only the garde was well kept.")

    rooftop = Room("rooftop")
    rooftop.set_name("Messy Rooftop")
    rooftop.set_description("One wrong step and... better not to think about that too much.")

    # Links the rooms together
    main_hall.link_room(dining_hall, "west"), dining_hall.link_room(main_hall, "east")
    main_hall.link_room(upper_main_hall, "up"), upper_main_hall .link_room(main_hall, "down")
    main_hall.link_room(art_gallery, "east"), art_gallery.link_room(main_hall, "west")
    main_hall.link_room(garden, "north"), garden.link_room(main_hall, "south")
    kitchen.link_room(dining_hall, "south"), dining_hall.link_room(kitchen, "north")
    dining_hall.link_room(ballroom, "west"), ballroom.link_room(dining_hall, "east")
    upper_main_hall.link_room(storeroom, "east"), storeroom.link_room(upper_main_hall, "west")
    upper_main_hall.link_room(bedroom, "west"), bedroom.link_room(upper_main_hall, "east")
    upper_main_hall.link_room(overlook, "north"), overlook.link_room(upper_main_hall, "south")
    bedroom.link_room(bathroom, "south"), bathroom.link_room(bedroom, "north")
    garden.link_room(hedge_maze, "north"), hedge_maze.link_room(garden, "south")
    garden.link_room(stable, "east"), stable.link_room(garden, "west")
    overlook.link_room(rooftop, "up"), rooftop.link_room(overlook, "down")

    # Initializes enemies
    dave = Enemy("Dave", "A smelly zombie.")
    dave.set_conversation("Brrlgrh... rgrhl... brains...")
    dave.set_weakness("cheese")

    vamp = Enemy("Vamp", "A classy vampire.")
    vamp.set_conversation("And you break into my property for what reason now?")
    vamp.set_weakness("flashlight")

    lobo = Enemy("Lobo", "A fierce looking wolf")
    lobo.set_conversation("...*you only get a piercing gaze in return*")
    lobo.set_weakness("knife")

    petit = Enemy("Petit", "A prank-loving fairy")
    petit.set_conversation(
        "What are you doing up here? Aren't you afraid of heights and... hey look behind you! A UFO!"
        )
    petit.set_weakness("horseshoe")

    # Initializes friends
    frank = Friend("Frank", "A fellow exterminator and also a good friend.")
    frank.set_conversation(
        f"We're still missing {Enemy.number_of_enemies} to fully clean this place up."
        )

    # Sets characters to their designed locations
    dining_hall.set_character(dave)
    main_hall.set_character(frank)
    art_gallery.set_character(vamp)
    hedge_maze.set_character(lobo)
    rooftop.set_character(petit)

    # Initializes items
    cheese = Item("cheese")
    cheese._name = "Cheese"
    cheese._interpretation = "Rotten and decayed cheese."

    flashlight = Item("flashlight")
    flashlight._name = "Flashlight"
    flashlight._interpretation = "Old but strong: works surprisingly well despite its age."

    knife = Item("knife")
    knife._name = "Knife"
    knife._interpretation = "It has a beautiful and well polished silver blade."

    horseshoe = Item("horseshoe")
    horseshoe._name = "Horseshoe"
    horseshoe._interpretation = "A single horseshoe made of cast iron."

    # Sets items to their designed locations
    kitchen.set_item(cheese)
    storeroom.set_item(flashlight)
    bathroom.set_item(knife)
    stable.set_item(horseshoe)

    # Initializes backpack
    backpack = []

    # Defines starting room
    current_room = main_hall

    # Loops the game until game over or victory conditions are reached
    loop_end = False

    # Runs the game
    while loop_end == False:
        print(" ")
        sleep(0.5)
        print("==========")
        print(f"You are in the {current_room.get_name()}.")
        current_room.get_details()
        # Uses the getter from room.py to store a character inside a room
        inhabitant = current_room.get_character()
        item = current_room.get_item()

        if inhabitant is not None:
            inhabitant.describe()
        else:
            print(" ")
         
        print(" ")      
        print(f"Your items: {backpack}")
        print(
            "Commands: [North], [South], [East], [West], [Up], [Down], [Examine], [Talk], [Fight], "
            "[Collect]"
            )
        command = input("> ")

        if (command == "north" or command == "south" or command == "east" or command == "west" 
        or command.lower() == "up" or command == "down"):
            current_room = current_room.move(command)

        elif command.lower() == "examine":
            current_room.describe()
            if item is not None:
                item.see_item()


        elif command.lower() == "talk":
            if inhabitant is not None:
                inhabitant.talk()
            else:
                print("There is nobody here.")

        elif command.lower() == "fight":
            if isinstance(inhabitant, Enemy) == True:
                if inhabitant is not None:
                    combat_item = input(f"> What will you fight {inhabitant.name} with? ")
                    if combat_item.capitalize() in backpack:                            
                        inhabitant.fight(combat_item)
                        if inhabitant.weakness.lower() == combat_item.lower():
                            print(f"{inhabitant.name} runs away!")
                            inhabitant.enemy_defeated(current_room)
                            
                            # Updates the amount of enemies warning
                            frank.set_conversation(
                            f"We're still missing {Enemy.number_of_enemies} to fully clean this place up."
                            )

                        else:
                            print("You lose! Game over!")
                            input("Press enter to close.")
                            loop_end = True
                            break
                    else:
                        print("That is not on your backpack!")
            elif isinstance(inhabitant, Friend):
                inhabitant.fight()
            else:
                print("There is nobody in this room for you to fight with.")
        
        elif command.lower() == "collect":
            if item is not None:
                item.collect(backpack, current_room)
            else:
                print("There's nothing to collect here!")

        else:
            print(
                f"{command.capitalize()} is not a command! "
                "Please type one of the commands in the list!"
                )

        # Checks victory conditions after every loop.
        if Enemy.number_of_enemies == 0:
            print("You defeated all enemies! Congratulations!")
            input("Press Enter to close.")
            loop_end == True
            break

        if loop_end == False:
            sleep(0.5)


if __name__ == "__main__":
    main()