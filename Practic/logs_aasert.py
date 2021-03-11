"""Площади фигур"""

c = int(input("Enter first side of rectangle: "))
b = int(input("Enter second side of rectangle: "))
print("Step 1: c = ", c, "; b = ", b)
Per = 2 * c + 2 * b
print("Step 2: Per = ", Per)
print(Per)

d = int(input("Enter  side of square: "))
assert d > 0
Sa = d * d
print(Sa)

r = int(input("Enter radius: "))
assert r > 0
Ca = 3.141592 * r * r
print(Ca)