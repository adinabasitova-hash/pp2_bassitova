class MyClass:
  def getString(self):
    self.a = input()
  def printString(self):
    print(self.a.upper())

obj = MyClass()
obj.getString()
obj.printString()