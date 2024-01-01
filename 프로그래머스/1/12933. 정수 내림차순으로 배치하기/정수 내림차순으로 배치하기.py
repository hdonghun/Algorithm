def solution(n):
    answer = 0
    result = []
    n = str(n)
    
    for i in n:
        result.append(int(i))
    result.sort(reverse=True)
    answer = int(''.join(map(str,result)))
    
    return answer
