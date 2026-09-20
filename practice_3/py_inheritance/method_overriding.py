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

# Here is method overriding, TrainingSession changes how speak works
class Session(Person):
    def speak(self):
        print(f"{self.name} session is starting")

s = Session("Morning swim")
s.speak()