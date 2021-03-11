from geometry.square import square_area
from geometry.circle.circle_area import circle_area
from geometry.rectangle.perimeter import perimeter as per

r = int(input("Enter radius: "))
print(circle_area(r))

a = int(input("Enter first side of rectangle: "))
b = int(input("Enter second side of rectangle: "))
print(per(a, b))

d = int(input("Enter  side of square: "))
print(square_area.square_area(d))