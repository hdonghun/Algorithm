temp = []
tt = ''

for i in range(5):
    temp.append(list(input()))

max_len = max(map(len, temp))

for i in range(max_len):
    for j in range(5):
        if i < len(temp[j]): 
            tt += temp[j][i]

print(tt) 
