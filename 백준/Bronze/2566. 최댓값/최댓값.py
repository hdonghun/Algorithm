max_value = 0
max_row, max_col = 0, 0

for i in range(9):
    row = list(map(int, input().split()))  
    for j in range(9):
        if row[j] >= max_value:
            max_value = row[j]
            max_row, max_col = i + 1, j + 1  

print(max_value)
print(max_row, max_col)
