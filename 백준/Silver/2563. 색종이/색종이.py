n = int(input())
paper = []

for _ in range(100):
    row = [0] *100
    paper.append(row)

for _ in range(n):
    x,y = map(int,input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            if i >= 100 or j >= 100:
                break
            paper[i][j] = 1
            
sum = 0

for row in range(100):
    sum += paper[row].count(1)

print(sum)
