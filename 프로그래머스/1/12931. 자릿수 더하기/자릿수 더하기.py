def solution(n):
    answer = 0

    t = len(str(n))
    
    for i in range(t):
        answer += n % 10
        n = n // 10 
    
    return answer