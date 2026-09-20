# Here is a class with a method that changes its own state
class Counter:
    def __init__(self):
        self.count = 0

    def increase(self):
        self.count += 1

c = Counter()
c.increase()
c.increase()
print(c.count)