import math
degree = float(input())
radian = (degree * math.pi)/180
print(radian)

#2
height = float(input('Please enter a height: '))
base1 = float(input('Enter a first base: '))
base2 = float(input('Enter the second base: '))
def calculateArea(height, base1, base2):
  area = 1/2 * (base1 + base2) * height
  print(area)

calculateArea(height, base1, base2)

#3
import math

n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

area = n * s ** 2 / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", area)

#4
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = base * height
print("Expected Output:", area)