def check(x, y, z):
    temp = [x, y, z]
    temp.sort()

    if temp[0] + temp[1] <= temp[2]:
        return "Invalid"
    elif x == y == z:
        return "Equilateral"
    elif x == y or y == z or z == x:
        return "Isosceles"
    else:
        return "Scalene"

while True:
    x, y, z = map(int, input().split())
    if x == 0 and y == 0 and z == 0:
        break
    
    result = check(x, y, z)
    print(result)
