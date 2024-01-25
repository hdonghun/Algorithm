def solution(n):
    answer = 0
    count_2 = 0
    count = bin(n)[2:].count('1')
    
    m = n+1
    while count != count_2:
        count_2 = bin(m)[2:].count('1')
        if count_2 == count:
            return m
        m = m+1