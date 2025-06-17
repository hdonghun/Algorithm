data = []
for i in range(5):
    line = input()
    data.append(line)

result = ''
for j in range(15): # 문제에서 명시적으로 "문자열 길이는 최대 15자까지 올 수 있다"고 주어짐 
    for i in range(5):
        if j < len(data[i]): # 지금 읽으려는 인덱스 j가 해당 줄의 길이보다 작을 때만 접근
            result += data[i][j]

print(result)