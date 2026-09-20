# Here is a basic class for an athlete
class Athlete:
    def __init__(self, name, sport):
        self.name = name
        self.sport = sport

    def introduce(self):
        print(f"Hi, I'm {self.name} and I do {self.sport}")

adina = Athlete("Adina", "tennis")
adina.introduce()
