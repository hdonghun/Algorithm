x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

temp_x = [x1, x2, x3]
temp_y = [y1, y2, y3]

for i in temp_x:
    if temp_x.count(i) == 1:
        x4 = i

for i in temp_y:
    if temp_y.count(i) == 1:
        y4 = i

print(x4, y4)
