n = int(input())
temp = list(map(int, input().split()))
total = 0
y = max(temp)

for i in range(n):
    total += temp[i] / y * 100

print(total / n)