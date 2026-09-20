class Shape:
 def area(self):
  print(0)
  
class Square(Shape):
 def __init__(self, length):
  self.length = length
 def area(self):
  print(self.length * self.length)

 #3
class Rectangle(Shape):
  def __init__(self, length, width):
   self.length = length
   self.width = width
  def area(self):
   print(self.length * self.width)

rect = Rectangle(3,4)
rect.area()
            
