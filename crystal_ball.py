class Crystal_Ball():
    def __init__(self) -> None:
        self.name = "Strange Orb"
        self.description = None
    
    def show_name(self):
        print(self.name)
    
    def examine(self):
        self.name = "Crystal Ball"
        self.description = "A clear sphere used by fortune tellers. May show you a glimpse of the future."
        print(self.name)
        print(self.description)

    def read_fortune(self, random_number):
        if random_number == 0:
            print(
                "You gaze through the crystal ball and see nothing.",
                "Either you lack the talents for clairvoyance or this whole thing is an elaborate fraud."
            )
        elif random_number == 1:
            print(
                "You gaze through the crystal ball and see cold shades of white and grey.",
                "It looks as if you'll confront an approaching storm soon. Maybe bring an umbrella with you.",
                "Or perhaps the storm may symbolize an upcoming disaster that will shake your whole worldview.",
                 "Hard to tell at a glance."
            )
        elif random_number == 2:
            print(
                "You gaze through the crystal ball and see a bright, incandescent, warm light.",
                "Sounds like good things are coming your way!",
                "Well, either that or an your eyesight severely suffering from staring at the Sun",
                "a little too much. You shouldn't do that."
            )
        elif random_number == 3:
            print(
                "You gaze through the crystal ball and see a bunch of bright colors clashing against each",
                "other. This surely means something, you think to yourself; but what could that be?",
            )

    def pick_up(self, inventory):
        print(f"You pick up the {self.name}.")
        inventory.append(self.name)