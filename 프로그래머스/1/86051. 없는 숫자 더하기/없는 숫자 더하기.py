def solution(numbers):
    result = [0,1,2,3,4,5,6,7,8,9]
    answer = 0

    for i in numbers:
        if i in result:
            result.remove(i)

    for i in result:
        answer += i
             
    return answer