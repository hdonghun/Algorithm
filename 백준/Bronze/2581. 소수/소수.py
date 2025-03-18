x=int(input())
y=int(input())
temp = []
for i in range(x, y+1):
    if i < 2:
        continue
    suso = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            suso = False
            break
    if suso:
        temp.append(i)

if not temp:
    print(-1)
else:
    print(sum(temp))
    print(min(temp))
    