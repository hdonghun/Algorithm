def solution(x):
    answer= 0
    for i in str(x):
        answer += int(i)

    return x % answer == 0