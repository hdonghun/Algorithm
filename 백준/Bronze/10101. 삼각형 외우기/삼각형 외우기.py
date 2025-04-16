x = int(input())
y = int(input())
z = int(input())

if x == y == z == 60:
    print("Equilateral")
elif (x + y + z == 180) and (x == y or y == z or z == x):
    print("Isosceles")
elif (x + y + z == 180) and (x != y and y != z and z != x):
    print("Scalene")
elif x + y + z != 180:
    print("Error")
