# Here is basic inheritance, Coach is kinda like Athlete but with extra stuff
class Person:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} says hi")

class Coach(Person):
    def __init__(self, name, section):
        super().__init__(name)
        self.section = section

coach1 = Coach("Timur", "Swimming")
coach1.speak()
print(coach1.section)