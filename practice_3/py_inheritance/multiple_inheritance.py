# Here is multiple inheritance, mixing two unrelated classes together
class CanSwim:
    def swim(self):
        print("swimming now")

class CanRun:
    def run(self):
        print("running now")

class Triathlete(CanSwim, CanRun):
    pass

t = Triathlete()
t.swim()
t.run()