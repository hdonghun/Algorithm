def solution(s):
    answer = 0
    numbers = s.split()

    # 숫자와 "Z"를 올바르게 처리
    for i in range(len(numbers)):
        if numbers[i] == "Z":
            answer -= int(numbers[i-1])
        else:
            answer += int(numbers[i])
        print(answer)
    return answer
