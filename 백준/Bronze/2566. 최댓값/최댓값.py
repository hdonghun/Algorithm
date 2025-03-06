record = [0, 0, 0]

for i in range(9):
    max_number = list(map(int, input().split()))
    for j in range(9):
        if max_number[j] >= record[0]:
            record = [max_number[j], i + 1, j + 1]

print(record[0])
print(record[1], record[2])
