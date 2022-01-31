class RPGInfo():
    author = "Anonymous"

    def __init__(self, game_title) -> None:
        self.title = game_title
    
    def welcome(self):
        print(f"Welcome to '{self.title}'.")

    @staticmethod
    def info():
        print(
            "Monsters have overrun this old and dilapidated mansion that was supposed to become the "
            "latest tourist attraction. Chase them away!"
            )

    @classmethod
    def credits(cls):
        print("Thank you for playing!", end=" ")
        print(f"Created by {cls.author}.")