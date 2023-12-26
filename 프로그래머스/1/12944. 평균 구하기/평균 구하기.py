def solution(arr):
    answer = 0
    result = 0
    for i in arr:
        answer+=i
    result = answer / len(arr)
    return result