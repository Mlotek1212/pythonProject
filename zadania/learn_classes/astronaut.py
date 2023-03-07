class Person:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def walk(self):
        print("I can walk")


class Astronaut(Person):
    def fly(self):
        print("I fly in the space")

    def walk(self):
        print("I can walk on earth and on moon")


mark = Astronaut("Mark", "Kowalski")
breakpoint()
pass
