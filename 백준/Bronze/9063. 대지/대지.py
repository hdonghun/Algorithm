n = int(input())
temp_x = []
temp_y = []
if n < 1:
    print(0)
else:
    for i in range(n): 
        x,y = map(int, input().split())
        temp_x.append(x)
        temp_y.append(y)
     
    result = (max(temp_x) - min(temp_x)) * (max(temp_y)-min(temp_y))
    print(result)