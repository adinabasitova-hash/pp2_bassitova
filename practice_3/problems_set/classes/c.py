class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def show(self):
        print(f'Coordinate 1: {self.a}, Coordinate 2: {self.b}')

    def move(self):
        print('By how much do you want to change the coordinate 1?')
        c = int(input())
        self.a = self.a + c

        print('By how much do you want to change the coordinate 2?')
        d = int(input())
        self.b = self.b + d

        print(f'New coordinates are {self.a} and {self.b}')

    def dist(self, point):
     return ((self.a - point.a) ** 2 + (self.b - point.b) ** 2) ** 0.5

p1 = Point(0, 0)
p2 = Point(3, 4)
print(p1.move())