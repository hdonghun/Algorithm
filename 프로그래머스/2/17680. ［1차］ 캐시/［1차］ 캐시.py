def solution(cacheSize, cities):
    answer = 0
    temp_0 = []
    temp = []
    
    for i in cities:
        temp_0.append(i.lower())
        
    for i in range(len(temp_0)):
        if cacheSize == 0:
            temp.append(temp_0[i])
            answer += 5
        else: 
            if temp_0[i] not in temp:
                if len(temp) >= cacheSize:
                    temp.pop(0)
                    temp.append(temp_0[i])
                    answer += 5
                else:
                    temp.append(temp_0[i]) 
                    answer += 5
            else:
                temp.remove(temp_0[i])
                temp.append(temp_0[i])
                answer += 1

    return answer