def solution(arr):
    answer = arr[0]
    
    for i in range(1, len(arr)):
        answer = calculate_lcm(answer, arr[i])
    
    return answer

def calculate_lcm(a, b):
    # 최소공배수를 계산하는 함수
    # a와 b의 곱을 최대공약수로 나누면 최소공배수가 됨
    return a * b // calculate_gcd(a, b)

def calculate_gcd(a, b):
    # 최대공약수를 계산하는 함수
    # 유클리드 호제법 사용
    while b:
        a, b = b, a % b
    return a