temp = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

total_score = 0
total_rhkahr = 0
for i in range(20):
    x, y, z = input().rsplit(maxsplit=2)
    y = float(y)
    if z in temp:
        total_score += y * temp[z]
        total_rhkahr += y

print(total_score / total_rhkahr)

