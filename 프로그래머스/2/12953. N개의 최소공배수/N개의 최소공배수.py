def solution(arr):
    answer = arr[0]
    
    for i in range(1, len(arr)):
        answer = calculate_lcm(answer, arr[i])
    
    return answer

def calculate_lcm(a, b):
    return a * b // calculate_gcd(a, b)

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a