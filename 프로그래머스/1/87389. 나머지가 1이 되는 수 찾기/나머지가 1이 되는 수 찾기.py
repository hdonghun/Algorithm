def solution(n):
    answer = 0
    result = []
    
    for i in range(1, n+1):
        if n % i == 1:
            result.append(i)
    answer = min(result)
    return answer