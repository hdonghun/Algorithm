def sosu(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    temp_list = set()
    def jegi(curr, next):
        if curr:
            temp_list.add(int(curr))
        for i in range(len(next)):
            jegi(curr + next[i], next[:i] + next[i+1:])
    
    jegi("", numbers)
    
    sosu_count = sum(1 for num in temp_list if sosu(num))
    return sosu_count
