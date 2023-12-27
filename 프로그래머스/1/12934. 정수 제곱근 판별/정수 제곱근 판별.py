import math

def solution(n):
    x = math.isqrt(n)  # 정수 제곱근을 구함

    if x**2 == n:  # n이 양의 정수 x의 제곱인 경우
        return (x + 1)**2
    else:
        return -1