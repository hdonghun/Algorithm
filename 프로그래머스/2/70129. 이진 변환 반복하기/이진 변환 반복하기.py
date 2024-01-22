def solution(s):
    answer = []
    count = 0 
    result = 0
    
    while s != "1":  
        for i in s:
            if i == '0':
                s = s.replace('0', '')
                count += 1
        s = bin(len(s))[2:] 
        result += 1
    answer = [result, count]
    return answer